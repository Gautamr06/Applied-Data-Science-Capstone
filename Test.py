# Mini Falcon 9 Launch Analysis

launches = [
    {"mission": "Starlink-15", "landing_success": True},
    {"mission": "GPS III", "landing_success": False},
    {"mission": "Crew-1", "landing_success": True},
    {"mission": "Starlink-16", "landing_success": True},
    {"mission": "Satellite-X", "landing_success": False},
    {"mission": "Cargo Resupply", "landing_success": True},
]

print("🚀 Falcon 9 Launch Landing Analysis\n")

total_launches = len(launches)
successful_landings = 0

for launch in launches:
    status = "Success" if launch["landing_success"] else "Failure"
    print(f"Mission: {launch['mission']} → Landing: {status}")
    
    if launch["landing_success"]:
        successful_landings += 1

success_rate = (successful_landings / total_launches) * 100

print("\n📊 Summary")
print(f"Total Launches: {total_launches}")
print(f"Successful Landings: {successful_landings}")
print(f"Landing Success Rate: {success_rate:.2f}%")

if success_rate > 60:
    print("\n💰 Insight: High reuse rate → Lower launch cost")
else:
    print("\n⚠️ Insight: Low reuse rate → Higher launch cost")
