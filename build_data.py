import json
H = json.load(open('/tmp/claude-0/-home-claude/50526bc3-3f4b-5ccc-9f93-15275bd094e4/scratchpad/hotspots.json'))
from PIL import Image

SECTIONS = [
    {"id": "sling", "name": "Sling Load Equipment", "short": "Sling Load"},
    {"id": "a22", "name": "A-22 Cargo Bag", "short": "A-22"},
    {"id": "nets", "name": "5K and 10K Cargo Nets", "short": "Cargo Nets"},
    {"id": "m1101", "name": "M1101 Trailer", "short": "M1101"},
    {"id": "m1151", "name": "M1151 HMMWV", "short": "M1151"},
    {"id": "blivet", "name": "Triple Blivets", "short": "Blivets"},
    {"id": "isv", "name": "M1301 ISV", "short": "ISV"},
]

# id: (name, section, cap, lp, size, note)   cap/lp in lbs (int) ; size string ; note string (not testable info)
I = {}
def item(id, name, sec, cap=None, lp=None, size=None, note=None, alias=None):
    I[id] = {"name": name, "sec": sec, "cap": cap, "lp": lp, "size": size, "note": note, "alias": alias}

# --- Sling load equipment
item("xxvi", "Aerial Delivery Sling, Type XXVI (Multi-Loop Line)", "sling", note="Rated capacity depends on number of loops and whether it is used as a pendant or as a lifting provision. See the Tables tab.")
item("donut", "3 Foot Apex Ring (Donut Ring)", "sling", cap=10000, note="Aerial Delivery Sling with Type IV Connector Link")
item("typeiv", "Type IV Connector Link", "sling", cap=12500)
item("baseplate", "Base Plate", "sling", note="Part of the Type IV Connector Link")
item("albuffer", "Aluminum Buffers", "sling", note="Part of the Type IV Connector Link")
item("lockplate", "Locking Plate", "sling", note="Part of the Type IV Connector Link")
item("cottonbuffer", "Cotton Buffer", "sling", note="Sleeve on the donut ring")
item("twopoint", "Two Point Link Assembly", "sling", cap=25000)
item("clevis_s", "Small Suspension Clevis", "sling", cap=6250, lp=3750)
item("clevis_m", "Medium Suspension Clevis", "sling", cap=6250, lp=3750)
item("clevis_l", "Large Suspension Clevis", "sling", cap=12500, lp=7875)
item("nut", "Nut", "sling", note="Suspension clevis hardware")
item("bolt", "Bolt", "sling", note="Suspension clevis hardware")
item("a7a", "A7A Strap", "sling", cap=500)
item("friction", "Friction Adapter", "sling")
item("cgu", "CGU-1/B", "sling", cap=5000)
item("dacron", "15 Foot Tie-Down Strap (Dacron Lashings)", "sling", cap=10000)
item("dring", "D-Ring", "sling")
item("binder_silver", "Silver Load Binder", "sling", cap=5000)
item("binder_black", "Black Load Binder", "sling", cap=10000)
item("screwpin", "Screw Pin", "sling", note="Part of the 5/8 in Screw Pin Clevis")
item("cotter", "Cotter Pin", "sling")
item("clevis58", "5/8 Inch Screw Pin Clevis", "sling", cap=4420)
item("apex10", "10,000 lbs Apex Fitting", "sling", cap=10000)
item("leg10", "10,000 lbs Sling Leg", "sling", cap=2500, note="Rated capacity is per leg")
item("chain", "Chain", "sling", note="Part of the sling leg")
item("grabhook", "Grabhook Assembly", "sling")
item("apex25", "25,000 lbs Apex Fitting", "sling", cap=25000)
item("leg25", "25,000 lbs Sling Leg", "sling", cap=6250, note="Rated capacity is per leg")
item("apexpin10", "Apex Fitting Pin (10,000 lbs)", "sling", cap=10000, size="1 1/8 inch", note="Pin for the 10,000 lbs apex fitting")
item("apexpin25", "Apex Fitting Pin (25,000 lbs)", "sling", cap=25000, size="1 1/2 inch", note="Pin for the 25,000 lbs apex fitting")
item("apexspacer", "Apex Spacer", "sling")
item("apexshackle10", "Apex Shackle (10,000 lbs)", "sling", cap=10000)
item("apexshackle25", "Apex Shackle (25,000 lbs)", "sling", cap=25000)
item("castnut", "Castellated Nut", "sling")
item("drilledbolt", "3/8 Inch Drilled Bolt", "sling", size="3/8 inch")
item("gh_bolt", "Bolt and Dome Nut / Locking Nut", "sling", note="Grabhook assembly")
item("gh_keeper", "Keeper", "sling", note="Grabhook assembly")
item("gh_hook", "Hook", "sling", note="Grabhook assembly")
item("gh_pin", "Pin", "sling", note="Grabhook assembly")
item("gh_yoke", "Yoke", "sling", note="Grabhook assembly")
item("gh_eye", "Eye", "sling", note="Grabhook assembly")
item("gh_coupling", "Coupling Link", "sling", note="Grabhook assembly")
item("gh_spacer", "Spacer", "sling", note="Grabhook assembly")
item("gh_snap", "Snap Ring", "sling", note="Grabhook assembly")
item("pendant25", "25,000 lbs Cargo Hook Reach Pendant", "sling", cap=25000)
item("pendant11", "11,000 lbs Cargo Hook Reach Pendant", "sling", cap=11000)
item("pend_large", "Large Looped End (towards the load)", "sling", note="Reach pendant")
item("pend_arrow", "Directional Arrow", "sling", note="Reach pendant")
item("pend_handle", "Handle", "sling", note="Reach pendant")
item("pend_small", "Small Looped End (towards the aircraft)", "sling", note="Reach pendant")
item("roundsling", "Polyester Round Sling", "sling", note="Rated capacity depends on color and hitch type. See the Tables tab.")
item("idtag", "Identification Tag", "sling", note="At least one must be present and legible")
# --- A-22
item("a22", "A-22 Cargo Bag", "a22")
item("lateral", "Lateral Strap", "a22")
item("strap188", "188” Strap", "a22", size="188 inches")
item("scuff", "Scuff Pad", "a22")
item("canvas", "Canvas Cover (Optional)", "a22")
item("web24", "24” Suspension Web", "a22", cap=550, size="24 inches", note="Rated capacity is 550 lbs each")
item("lacing", "Lacing Cord", "a22")
item("exlateral", "Excess Lateral Strap", "a22")
item("ex188", "Excess 188” Strap", "a22")
item("snap", "Connector Snap", "a22")
# --- Nets
item("net5", "5,000 lbs Cargo Net", "nets", cap=5000, size="15 ft x 15 ft; mesh 6 in x 6 in")
item("lz5", "Load Zone (5,000 lbs net)", "nets", size="5 ft x 5 ft")
item("net10", "10,000 lbs Cargo Net", "nets", cap=10000, size="18 ft x 18 ft; mesh 7.5 in x 7.5 in")
item("lz10", "Load Zone (10,000 lbs net)", "nets", size="6 ft x 6 ft")
item("liftleg", "Lifting Leg", "nets")
item("nethook", "Hook", "nets", note="Hooks must be taped")
item("netapex", "Net Apex Fitting", "nets", cap=10000)
item("breakaway", "Breakaway Tie", "nets")
item("tether", "Net Apex Tether Cord", "nets")
# --- M1101
item("felt", "Cattle Hair Felt", "m1101")
item("t_pbrake", "Parking Brake", "m1101")
item("lunette", "Lunette", "m1101")
item("frontjack", "Front Jack", "m1101")
item("safetychains", "Safety Chains", "m1101")
item("t_dataplate", "Data Plate", "m1101")
item("lightcable", "Light Cable", "m1101")
item("t_cgu", "CGU-1/B", "m1101", cap=5000)
item("t_a7a", "A7A Strap", "m1101", cap=500)
item("t_load", "Load", "m1101")
item("stabilizer", "Stabilizer Leg", "m1101")
item("tailgate", "Tailgate Latch", "m1101")
item("mfgpin", "Manufactured Pin", "m1101")
# --- M1151
item("turret", "Turret", "m1151")
item("h_wheels", "Wheels", "m1151")
item("h_fuelcap", "Fuel Cap", "m1151")
item("h_hoodlatch", "Hood Latch", "m1151")
item("h_dataplate", "Data Plate", "m1151")
item("h_cluster", "Instrument Cluster", "m1151")
item("h_wheel", "Steering Wheel", "m1151")
item("h_cable", "Cable", "m1151")
item("h_lock", "Lock", "m1151")
item("enginelatch", "Engine Cover Latch", "m1151")
item("h_pbrake", "Parking Brake", "m1151")
item("transsel", "Transmission Selector", "m1151")
item("turretlock", "Turret Lock", "m1151")
item("turretlatch", "Turret Latch", "m1151")
item("turrethandle", "Turret Handle", "m1151")
item("batterylatch", "Battery Box Latch (under passenger seat)", "m1151")
# --- Blivets
item("bezel", "Bezel Ring", "blivet")
item("nozzle", "Fuel Nozzle", "blivet")
item("nozzle_taped", "Fuel Nozzle (covered with 2 in tape)", "blivet")
item("b_clevis58", "5/8” Screw Pin Clevis", "blivet", cap=4420)
item("b_cotter", "Cotter Pin", "blivet")
item("clusterbreak", "Cluster Breakaway", "blivet")
item("b_fuelcap", "Fuel Cap", "blivet")
# --- ISV
item("hoodpins", "Hood Pins", "isv")
item("i_wheels", "Wheels", "isv")
item("wsmount", "Windshield Mount", "isv")
item("i_hoodlatch", "Hood Latch", "isv")
item("i_cluster", "Instrument Cluster", "isv")
item("i_wheel", "Steering Wheel", "isv")
item("i_pbrake", "Parking Brake", "isv")
item("litter", "Litter Rail", "isv")
item("seats", "Seats Stowed", "isv")
item("bii", "BII Box", "isv")
item("fueldoor", "Fuel Fill Door", "isv")
item("rops", "Roll Over Protection System (ROPS)", "isv")

# ---- Figures: (id, section, title, image, slide key, legend {n: item}, note)
F = []
def fig(id, sec, title, img, key, legend, note=None, override=None, tables=None):
    hs = [h for h in H.get(key, []) if h['img'] == img]
    out = []
    for h in hs:
        if h['n'] not in legend: continue
        x, y = h['x'], h['y']
        if override and h['n'] in override: x, y = override[h['n']]
        out.append({"n": h['n'], "x": x, "y": y, "item": legend[h['n']]})
    # any legend entries with no hotspot and an override -> add
    present = {o['n'] for o in out}
    for n, it in legend.items():
        if n not in present and override and n in override:
            x, y = override[n]; out.append({"n": n, "x": x, "y": y, "item": it})
    im = Image.open(f'/home/claude/nomen/img/{img}.jpg')
    F.append({"id": id, "sec": sec, "title": title, "img": f"img/{img}.jpg", "w": im.width, "h": im.height,
              "hs": out, "legend": [{"n": n, "item": it} for n, it in legend.items()], "note": note, "tables": tables or []})

# Sling load
fig("f_xxvi", "sling", "Aerial Delivery Sling, Type XXVI", "p1_s004_1", "p14", {"1": "xxvi"}, override={"1": (0.5, 0.5)},
    note="Rated capacities and available lengths are in the tables below.", tables=["xxvi_cap","xxvi_len"])
fig("f_donut", "sling", "3 Foot Apex Ring (Donut Ring)", "p1_s005_0", "p15", {"1": "donut", "2": "typeiv"}, override={"2": (0.5, 0.17)})
fig("f_typeiv", "sling", "Type IV Connector Link", "p1_s005_3", "p15", {"2": "typeiv"})
fig("f_typeiv_parts", "sling", "Type IV Connector Link, disassembled", "p1_s005_2", "p15", {"3": "baseplate", "4": "albuffer", "5": "lockplate"})
fig("f_cotton", "sling", "Cotton Buffer", "p1_s005_4", "p15", {"6": "cottonbuffer"})
fig("f_twopoint", "sling", "Two Point Link Assembly", "p1_s006_1", "p16", {"1": "twopoint"})
fig("f_clevis", "sling", "Suspension Clevises", "p1_s007_1", "p17", {"1": "clevis_s", "2": "clevis_m", "3": "clevis_l", "4": "nut", "5": "bolt"})
fig("f_tiedown1", "sling", "Cargo Tie-Down Equipment", "p1_s008_1", "p18", {"1": "a7a", "2": "friction", "3": "cgu"})
fig("f_tiedown2", "sling", "Cargo Tie-Down Equipment: Dacron lashing", "p1_s009_1", "p19", {"1": "dacron", "2": "dring"})
fig("f_binders", "sling", "Cargo Tie-Down Equipment: load binders", "p1_s009_2", "p19", {"3": "binder_silver", "4": "binder_black"})
fig("f_clevis58", "sling", "5/8 Inch Screw Pin Clevis", "p1_s010_0", "p110", {"1": "screwpin", "2": "cotter", "3": "clevis58"})
fig("f_leg10", "sling", "10,000 lbs Sling Leg", "p1_s011_1", "p111", {"1": "apex10", "2": "leg10", "3": "chain", "4": "grabhook"})
fig("f_leg25", "sling", "25,000 lbs Sling Leg", "p1_s012_1", "p112", {"1": "apex25", "2": "leg25", "3": "chain", "4": "grabhook"})
fig("f_apex10", "sling", "Apex Fitting, 10,000 lbs", "p1_s013_1", "p113", {"1a": "apexpin10", "2": "apexspacer", "3a": "apexshackle10", "4": "castnut", "5": "drilledbolt", "6": "cotter"})
fig("f_apex25", "sling", "Apex Fitting, 25,000 lbs", "p1_s013_2", "p113", {"1b": "apexpin25", "2": "apexspacer", "3b": "apexshackle25", "4": "castnut", "5": "drilledbolt", "6": "cotter"})
fig("f_grab1", "sling", "Grabhook Assembly", "p1_s014_1", "p114", {"1": "gh_bolt", "2": "gh_keeper", "3": "gh_hook", "4": "gh_pin", "5": "gh_yoke", "6": "gh_eye", "7": "gh_coupling"})
fig("f_grab2", "sling", "Grabhook Assembly, side view", "p1_s014_2", "p114", {"4": "gh_pin", "7": "gh_coupling", "8": "gh_spacer", "9": "gh_snap"})
fig("f_pend25", "sling", "25,000 lbs Cargo Hook Reach Pendant", "p1_s015_0", "p115", {"1": "pend_large", "2": "pend_arrow", "3": "pend_handle", "4": "pend_small"})
fig("f_pend11", "sling", "11,000 lbs Cargo Hook Reach Pendant", "p1_s016_0", "p116", {"1": "pend_large", "2": "pend_arrow", "3": "pend_handle", "4": "pend_small"})
fig("f_round", "sling", "Polyester Round Sling", "p1_s017_1", "p117", {"1": "idtag"}, note="Rated capacities by color and hitch type are in the table below.", tables=["round"])
# A-22
fig("f_a22_flat", "a22", "A-22 Cargo Bag, sling assembly laid flat", "p1_s020_0", "p120", {"1": "lateral", "2": "strap188", "3": "scuff", "4": "dring"})
fig("f_a22_cover", "a22", "A-22 Cargo Bag, cover and hardware", "p1_s020_1", "p120", {"5": "canvas", "6": "clevis_m", "7": "web24"})
fig("f_a22_rigged", "a22", "A-22 Cargo Bag, rigged", "p1_s021_0", "p121", {"1": "lateral", "2": "lacing", "3": "strap188", "4": "canvas"})
fig("f_a22_corner", "a22", "A-22 Cargo Bag, corner", "p1_s022_0", "p122", {"1": "lateral", "2": "lacing", "3": "friction", "4": "exlateral", "5": "canvas"})
fig("f_a22_side", "a22", "A-22 Cargo Bag, lateral strap detail", "p1_s023_0", "p123", {"1": "lateral", "2": "friction", "3": "exlateral", "4": "lacing"})
fig("f_a22_top", "a22", "A-22 Cargo Bag, top", "p1_s024_0", "p124", {"1": "lateral", "2": "friction", "3": "strap188", "4": "ex188", "5": "lacing", "6": "canvas"})
fig("f_a22_hang", "a22", "A-22 Cargo Bag, suspension point", "p1_s025_0", "p125", {"1": "clevis_m", "2": "dring", "3": "web24"})
fig("f_a22_webs", "a22", "24” Suspension Webs on the load", "p2_s001_0", "p21", {"1": "web24", "2": "snap", "3": "dring"})
fig("f_web24", "a22", "24” Suspension Web", "p2_s002_0", "p22", {"1": "web24", "2": "snap", "3": "dring"})
# Nets
fig("f_net5", "nets", "5,000 lbs Cargo Net", "p2_s004_1", "p24", {"1": "net5", "2": "liftleg", "3": "nethook", "5": "lz5"})
fig("f_netapex", "nets", "Net Apex Fitting", "p2_s004_2", "p24", {"4": "netapex"}, override={"4": (0.5, 0.5)})
fig("f_net10", "nets", "10,000 lbs Cargo Net", "p2_s005_1", "p25", {"1": "net10", "2": "liftleg", "3": "nethook", "4": "lz10"})
fig("f_net_rigged", "nets", "Cargo Net, rigged", "p2_s006_0", "p26", {"1": "netapex", "2": "nethook", "3": "breakaway", "4": "liftleg"})
fig("f_net_apex_detail", "nets", "Net Apex Fitting, detail", "p2_s007_0", "p27", {"1": "netapex", "2": "tether", "3": "nethook"}, note="Hooks must be taped (tape omitted in the picture to show the entire hook).")
# M1101
fig("f_t_front", "m1101", "M1101 Trailer, front", "p2_s009_0", "p29", {"1": "felt", "2": "t_pbrake", "3": "lunette", "4": "frontjack", "5": "safetychains", "6": "t_dataplate"})
fig("f_t_tongue", "m1101", "M1101 Trailer, tongue hardware", "p2_s010_0", "p210", {"1": "lunette", "2": "safetychains", "3": "lightcable"})
fig("f_t_bed", "m1101", "M1101 Trailer, bed with load", "p2_s011_0", "p211", {"1": "t_cgu", "2": "t_a7a", "3": "t_load"})
fig("f_t_rear", "m1101", "M1101 Trailer, rear", "p2_s012_0", "p212", {"1": "stabilizer", "2": "felt", "3": "tailgate"})
fig("f_t_rearcorner", "m1101", "M1101 Trailer, rear corner", "p2_s013_0", "p213", {"1": "mfgpin", "2": "tailgate", "3": "stabilizer"})
fig("f_t_stab", "m1101", "M1101 Trailer, stabilizer leg", "p2_s014_0", "p214", {"1": "stabilizer", "2": "mfgpin"})
fig("f_t_felt", "m1101", "Cattle Hair Felt", "p2_s015_0", "p215", {"1": "felt"})
# M1151
fig("f_h_front", "m1151", "M1151, front", "p2_s017_0", "p217", {"1": "turret", "2": "h_wheels"})
fig("f_h_fuel", "m1151", "M1151, fuel cap", "p2_s018_0", "p218", {"1": "h_fuelcap"})
fig("f_h_hood", "m1151", "M1151, hood latch", "p2_s019_0", "p219", {"1": "h_hoodlatch", "2": "h_wheels"})
fig("f_h_data", "m1151", "M1151, data plate", "p2_s020_0", "p220", {"1": "h_dataplate"})
fig("f_h_dash", "m1151", "M1151, dash", "p2_s021_0", "p221", {"1": "h_cluster", "2": "h_wheel", "3": "h_cable", "4": "h_lock"})
fig("f_h_console", "m1151", "M1151, center console", "p2_s022_0", "p222", {"1": "enginelatch", "2": "h_pbrake", "3": "transsel"})
fig("f_h_turretlock", "m1151", "M1151, turret lock", "p2_s023_0", "p223", {"1": "turretlock"})
fig("f_h_turret", "m1151", "M1151, turret ring", "p2_s024_0", "p224", {"1": "turretlatch", "2": "turrethandle", "3": "turretlock"})
fig("f_h_battery", "m1151", "M1151, battery box latch", "p2_s025_0", "p225", {"1": "batterylatch"})
# Blivets
fig("f_b_end", "blivet", "Triple Blivets, end", "p2_s027_0", "p227", {"1": "bezel", "2": "nozzle", "3": "b_clevis58", "4": "clusterbreak"})
fig("f_b_bezel", "blivet", "Triple Blivets, bezel ring detail", "p2_s028_0", "p228", {"1": "bezel", "2": "nozzle_taped", "3": "b_cotter", "4": "b_clevis58"})
fig("f_b_break", "blivet", "Cluster Breakaway", "p2_s029_0", "p229", {"1": "clusterbreak"})
fig("f_b_cap", "blivet", "Fuel Cap", "p2_s030_0", "p230", {"1": "b_fuelcap"}, override={"1": (0.5, 0.55)})
# ISV
fig("f_i_front", "isv", "M1301 ISV, front", "isv_s002_0", "isv2", {"1": "hoodpins", "2": "i_wheels"})
fig("f_i_ws", "isv", "M1301 ISV, windshield mount and hood latch", "isv_s003_0", "isv3", {"1": "wsmount", "2": "i_hoodlatch"})
fig("f_i_cluster", "isv", "M1301 ISV, instrument cluster", "isv_s004_0", "isv4", {"1": "i_cluster"}, override={"1": (0.5, 0.42)})
fig("f_i_wheel", "isv", "M1301 ISV, steering wheel", "isv_s005_0", "isv5", {"1": "i_wheel"})
fig("f_i_pbrake", "isv", "M1301 ISV, parking brake", "isv_s006_0", "isv6", {"1": "i_pbrake"})
fig("f_i_litter", "isv", "M1301 ISV, litter rail", "isv_s007_0", "isv7", {"1": "litter"})
fig("f_i_seats", "isv", "M1301 ISV, seats stowed and BII box", "isv_s008_0", "isv8", {"1": "seats", "2": "bii"})
fig("f_i_fuel", "isv", "M1301 ISV, fuel fill door", "isv_s009_0", "isv9", {"1": "fueldoor"})
fig("f_i_rops", "isv", "M1301 ISV, ROPS", "isv_s010_0", "isv10", {"1": "rops"})

TABLES = {
    "xxvi_cap": {"title": "Type XXVI Multi-Loop Line: rated capacity", "cols": ["Loops", "Pendant", "Lifting Provision"],
                 "rows": [["2", "8,900 lbs", "5,600 lbs"], ["3", "13,500 lbs", "8,500 lbs"], ["4", "17,800 lbs", "11,200 lbs"], ["6", "27,000 lbs", "17,000 lbs"]]},
    "xxvi_len": {"title": "Type XXVI Multi-Loop Line: lengths available", "cols": ["Loops", "Lengths"],
                 "rows": [["2", "3’, 9’, 11’, 12’, 16’, 20’, and 120’"], ["3", "60’ and 140’"], ["4", "3’, 9’, 11’, 12’, 16’, 20’, and 28’"], ["6", "60’ and 120’"]]},
    "round": {"title": "Polyester Round Sling: rated capacity by hitch type", "cols": ["Length", "Color", "Choked", "Vertical", "Basket", "Sling Weight"],
              "rows": [["8’", "Green", "4,200 lbs", "5,300 lbs", "10,600 lbs", "4 lbs"], ["17’", "Green", "4,200 lbs", "5,300 lbs", "10,600 lbs", "10 lbs"],
                       ["8’", "Yellow", "6,700 lbs", "8,400 lbs", "16,800 lbs", "5 lbs"], ["17’", "Yellow", "6,700 lbs", "8,400 lbs", "16,800 lbs", "11 lbs"],
                       ["30’", "Red", "10,600 lbs", "13,200 lbs", "26,400 lbs", "26 lbs"], ["65’", "Blue", "17,000 lbs", "21,200 lbs", "42,400 lbs", "75 lbs"],
                       ["70’", "Blue", "17,000 lbs", "21,200 lbs", "42,400 lbs", "81 lbs"]]},
}
# Table facts as quiz items: (id, question, answer, pool-key)
TF = []
for loops, pend, lp in [r for r in TABLES["xxvi_cap"]["rows"]]:
    TF.append({"id": f"xxvi_p{loops}", "q": f"Type XXVI, {loops}-loop, used as a pendant: rated capacity?", "a": pend, "pool": "xxvi", "sec": "sling"})
    TF.append({"id": f"xxvi_l{loops}", "q": f"Type XXVI, {loops}-loop, used as a lifting provision: rated capacity?", "a": lp, "pool": "xxvi", "sec": "sling"})
for loops, lens in TABLES["xxvi_len"]["rows"]:
    TF.append({"id": f"xxvi_len{loops}", "q": f"Type XXVI, {loops}-loop: which lengths are available?", "a": lens, "pool": "xxvi_len", "sec": "sling"})
seen = set()
for L, color, ch, v, b, w in TABLES["round"]["rows"]:
    if color in seen: continue
    seen.add(color)
    TF.append({"id": f"rs_{color}_ch", "q": f"{color} polyester round sling, choked hitch: rated capacity?", "a": ch, "pool": "round", "sec": "sling"})
    TF.append({"id": f"rs_{color}_v", "q": f"{color} polyester round sling, vertical hitch: rated capacity?", "a": v, "pool": "round", "sec": "sling"})
    TF.append({"id": f"rs_{color}_b", "q": f"{color} polyester round sling, basket hitch: rated capacity?", "a": b, "pool": "round", "sec": "sling"})
for L, color, ch, v, b, w in TABLES["round"]["rows"]:
    TF.append({"id": f"rs_len_{L}", "q": f"What color is the {L} polyester round sling?", "a": color, "pool": "color", "sec": "sling"})
# sizes
TF += [
    {"id": "sz_net5", "q": "5,000 lbs cargo net: overall size?", "a": "15 ft x 15 ft", "pool": "netsize", "sec": "nets"},
    {"id": "sz_net5m", "q": "5,000 lbs cargo net: mesh size?", "a": "6 in x 6 in", "pool": "mesh", "sec": "nets"},
    {"id": "sz_lz5", "q": "5,000 lbs cargo net: load zone size?", "a": "5 ft x 5 ft", "pool": "netsize", "sec": "nets"},
    {"id": "sz_net10", "q": "10,000 lbs cargo net: overall size?", "a": "18 ft x 18 ft", "pool": "netsize", "sec": "nets"},
    {"id": "sz_net10m", "q": "10,000 lbs cargo net: mesh size?", "a": "7.5 in x 7.5 in", "pool": "mesh", "sec": "nets"},
    {"id": "sz_lz10", "q": "10,000 lbs cargo net: load zone size?", "a": "6 ft x 6 ft", "pool": "netsize", "sec": "nets"},
    {"id": "sz_pin10", "q": "Apex fitting pin for the 10,000 lbs apex fitting: diameter?", "a": "1 1/8 inch", "pool": "pin", "sec": "sling"},
    {"id": "sz_pin25", "q": "Apex fitting pin for the 25,000 lbs apex fitting: diameter?", "a": "1 1/2 inch", "pool": "pin", "sec": "sling"},
    {"id": "sz_bolt", "q": "Drilled bolt in the apex fitting: size?", "a": "3/8 inch", "pool": "pin", "sec": "sling"},
    {"id": "sz_clevis", "q": "Screw pin clevis used on the blivets and tie-down equipment: size?", "a": "5/8 inch", "pool": "pin", "sec": "sling"},
    {"id": "sz_web", "q": "Suspension web on the A-22 cargo bag: length?", "a": "24 inches", "pool": "len", "sec": "a22"},
    {"id": "sz_188", "q": "Long strap on the A-22 cargo bag: length?", "a": "188 inches", "pool": "len", "sec": "a22"},
    {"id": "sz_dacron", "q": "Dacron lashing tie-down strap: length?", "a": "15 feet", "pool": "len", "sec": "sling"},
    {"id": "sz_donut", "q": "Apex ring (donut ring): size?", "a": "3 feet", "pool": "len", "sec": "sling"},
    {"id": "sz_tape", "q": "Blivet fuel nozzle is covered with tape of what width?", "a": "2 inches", "pool": "len", "sec": "blivet"},
]
POOLS = {
    "xxvi": ["8,900 lbs", "5,600 lbs", "13,500 lbs", "8,500 lbs", "17,800 lbs", "11,200 lbs", "27,000 lbs", "17,000 lbs"],
    "xxvi_len": [r[1] for r in TABLES["xxvi_len"]["rows"]],
    "round": sorted({c for r in TABLES["round"]["rows"] for c in r[2:5]}),
    "color": ["Green", "Yellow", "Red", "Blue"],
    "netsize": ["15 ft x 15 ft", "18 ft x 18 ft", "5 ft x 5 ft", "6 ft x 6 ft", "12 ft x 12 ft", "20 ft x 20 ft"],
    "mesh": ["6 in x 6 in", "7.5 in x 7.5 in", "5 in x 5 in", "8 in x 8 in", "4 in x 4 in"],
    "pin": ["1 1/8 inch", "1 1/2 inch", "3/8 inch", "5/8 inch", "1 1/4 inch", "3/4 inch", "1/2 inch"],
    "len": ["24 inches", "188 inches", "15 feet", "3 feet", "2 inches", "20 feet", "12 inches", "36 inches", "120 inches", "4 feet"],
}

DATA = {"sections": SECTIONS, "items": I, "figures": F, "tables": TABLES, "facts": TF, "pools": POOLS}
js = json.dumps(DATA, ensure_ascii=False, separators=(',', ':'))
open('/home/claude/nomen/data.json', 'w').write(js)
# sanity
used = {h['item'] for f in F for h in f['hs']}
print('items', len(I), 'figures', len(F), 'hotspots', sum(len(f['hs']) for f in F), 'facts', len(TF))
print('items never shown in a figure:', sorted(set(I) - used))
for f in F:
    missing = [l['n'] for l in f['legend'] if l['n'] not in {h['n'] for h in f['hs']}]
    if missing: print('figure', f['id'], 'legend entries with no hotspot:', missing)
