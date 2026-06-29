# ============================================================================
#  SCARICO ISTR_LAV_PEN_2_TV_4 v0.2 — condizione lavorativa × cittadinanza
#  CSD · CORREZIONE del v0.1 (che aveva collassato le dimensioni vive)
#  v0.2: CITIZENSHIP e CUR_ACT_STAT ora APERTE (erano fissate a TOTAL e 99).
#  Postino: copia tutto, incolla in Carnets, Run.
#  Output: ISTAT/limbo/tv4_lav_g/ -> zip automatico a fine run.
# ============================================================================

import sdmx, time, os, re, glob, shutil, collections
import pandas as pd

FLOW     = "DF_DCSS_ISTR_LAV_PEN_2_TV_4"
VERSIONE = "tv4_v0.2"   # timbro: identifica la versione che possiede questa cartella
G0       = 8
LIMBO    = "ISTAT/limbo"
CH       = LIMBO + "/tv4_lav_g"
COMUNI_F = LIMBO + "/comuni_list.txt"
DONE_F   = CH + "/_done.txt"
VERS_F   = CH + "/_versione.txt"

# --- Timbro di versione (standard CSD) -------------------------------------
# Pulisce la cartella SOLO se appartiene a una versione diversa (o assente).
# Se il timbro coincide, e' una ripartenza vera: non tocca nulla.
def _timbro_attuale():
    if os.path.isfile(VERS_F):
        return open(VERS_F).read().strip()
    return None
if os.path.isdir(CH) and _timbro_attuale() != VERSIONE:
    print(f"[TIMBRO] cartella di versione diversa ({_timbro_attuale()}): la svuoto per {VERSIONE}.")
    shutil.rmtree(CH)
os.makedirs(CH, exist_ok=True)
if _timbro_attuale() != VERSIONE:
    open(VERS_F, "w").write(VERSIONE + "\n")   # timbro PRIMA del primo scarico
    print(f"[TIMBRO] cartella marcata {VERSIONE}, parto pulito.")
else:
    print(f"[TIMBRO] {VERSIONE} confermato: riprendo dai file esistenti.")
# ---------------------------------------------------------------------------

# v0.2: tolte CITIZENSHIP e CUR_ACT_STAT dai FISSI -> restano libere (assi vivi).
# Fissate solo le dimensioni che la mappa (Manuale §17.14) dichiara collassate.
FISSI = {
    "INDICATOR":     "RESPOP_AV",
    "GENDER":        "T",
    "AGE_NOCLASS":   "Y_GE15",
    "EDU_ATTAIN":    "ALL",
    "LOC_DEST":      "ALL",
    "REAS_COMMUTING":"ALL",
}

INTERVALLO = 12.5; _last = [0.0]
def freno():
    a = INTERVALLO - (time.time() - _last[0])
    if a > 0: time.sleep(a)
    _last[0] = time.time()

ISTAT = sdmx.Client("ISTAT", timeout=300)

def chiama(fn, attempts=4, base=8):
    for k in range(attempts):
        freno()
        try:
            return fn()
        except Exception as e:
            if "404" in str(e): raise
            code = getattr(getattr(e, "response", None), "status_code", None)
            if code == 400 or "400 Client Error" in str(e): raise
            if k == attempts - 1: raise
            w = base * (k + 1)
            print(f"      rete? {type(e).__name__}: ritento tra {w}s ({k+1}/{attempts-1})")
            time.sleep(w)

if os.path.exists(COMUNI_F):
    comuni = [l.strip() for l in open(COMUNI_F) if l.strip()]
    print(f"elenco comuni su file: {len(comuni)}")
else:
    print("scarico CL_ITTER107...")
    try:
        cl = chiama(lambda: ISTAT.codelist("CL_ITTER107").codelist["CL_ITTER107"])
    except Exception as e:
        print(f"  RETE: CL non scaricabile. Cambia rete e rilancia.")
        raise SystemExit
    comuni = sorted(c for c in cl.items if re.fullmatch(r"\d{6}", c))
    open(COMUNI_F, "w").write("\n".join(comuni))
    print(f"  {len(comuni)} comuni salvati.")

done = {l.strip() for l in open(DONE_F) if l.strip()} if os.path.exists(DONE_F) else set()
todo = [c for c in comuni if c not in done]
TOT  = len(comuni)
print(f"gia' fatti {len(done)} · da fare {len(todo)} · lotti da {G0}")
if not todo:
    z = shutil.make_archive(LIMBO + "/tv4_lav_g", "zip", CH)
    print(f"GIA' TUTTO FATTO. Zip: {z} ({round(os.path.getsize(z)/1e6,1)} MB)")
    raise SystemExit

def tidy(s):
    if isinstance(s, pd.DataFrame):
        s = s.iloc[:, 0] if s.shape[1] else s.squeeze()
    df = s.rename("valore").reset_index()
    ren = {"REF_AREA":"territorio", "GENDER":"sesso",
           "CITIZENSHIP":"cittadinanza", "CUR_ACT_STAT":"cond_lav",
           "TIME_PERIOD":"anno"}
    df = df.rename(columns={k:v for k,v in ren.items() if k in df.columns})
    keep = ["territorio","sesso","cittadinanza","cond_lav","anno","valore"]
    return df[[c for c in keep if c in df.columns]]

counter = len(glob.glob(CH + "/g_*.csv"))
def salva(df):
    global counter
    df.to_csv(f"{CH}/g_{counter:04d}.csv", index=False); counter += 1
def marca(codes):
    with open(DONE_F, "a") as f: f.write("\n".join(codes) + "\n")
VUOTO = lambda: pd.DataFrame(columns=["territorio","sesso","cittadinanza","cond_lav","anno","valore"])

queue = collections.deque(todo[i:i+G0] for i in range(0, len(todo), G0))
fatti = vuoti = spezzati = 0; hardfail = 0
done0 = len(done); fatti_com = 0; t0 = time.time(); lotti = 0

def clock(): return f"{(time.time()-t0)/60:.1f}min"

print("=" * 72)
while queue:
    g = queue.popleft()
    key = dict(FISSI); key["REF_AREA"] = "+".join(g)
    try:
        df = tidy(chiama(lambda: sdmx.to_pandas(ISTAT.data(FLOW, key=key))))
        salva(df); marca(g); fatti += 1; fatti_com += len(g); hardfail = 0; lotti += 1
        nc = df["territorio"].nunique() if "territorio" in df.columns else 0
        print(f"  ok · {len(g):>2} com -> {len(df):>5} righe ({nc} con dati) · restano {len(queue)} lotti · {clock()}")
    except Exception as e:
        m = str(e); code = getattr(getattr(e, "response", None), "status_code", None)
        if code == 400 or "400 Client Error" in m:
            if len(g) <= 1:
                salva(VUOTO()); marca(g)
                print(f"  ⚠ comune {g} sfora da solo: marcato · {clock()}")
            else:
                h = len(g)//2; queue.appendleft(g[h:]); queue.appendleft(g[:h]); spezzati += 1
                print(f"  · lotto da {len(g)} -> spezzo in {h}+{len(g)-h} · {clock()}")
            hardfail = 0
        elif "404" in m:
            salva(VUOTO()); marca(g); vuoti += 1; fatti_com += len(g); hardfail = 0; lotti += 1
            print(f"  · {len(g)} com -> 404 (vuoto) · {clock()}")
        else:
            hardfail += 1; queue.append(g)
            print(f"  ✗ rete, lotto rimandato ({type(e).__name__}) · consecutivi {hardfail} · {clock()}")
            if hardfail >= 3:
                print("\n  RETE GIU': mi fermo. Rilancia (riprende dai file).")
                break
    if lotti and lotti % 20 == 0:
        el = (time.time()-t0)/60
        rate = fatti_com/el if el > 0 else 0
        eta_r = (TOT - done0 - fatti_com)/rate if rate > 0 else 0
        pct = 100*(done0+fatti_com)/TOT
        print(f"  — {done0+fatti_com}/{TOT} comuni · {pct:.0f}% · {el:.1f}min · ~{eta_r:.0f}min rimasti —")

done2 = {l.strip() for l in open(DONE_F) if l.strip()} if os.path.exists(DONE_F) else set()
print("\n" + "="*72)
print(f"sessione: {fatti} lotti · {spezzati} spezzati · {vuoti} vuoti · comuni {len(done2)}/{TOT} · {clock()}")
if set(comuni) <= done2:
    z = shutil.make_archive(LIMBO + "/tv4_lav_g", "zip", CH)
    print(f"COMPLETO! Zip da ripassarmi: {z} ({round(os.path.getsize(z)/1e6,1)} MB)")
else:
    print(f"Mancano {TOT-len(done2)} comuni. Rilancia: riprende dai file, salta i fatti.")
