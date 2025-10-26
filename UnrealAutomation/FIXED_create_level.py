"""
FIXED VERSION - Creates a simple multiplayer level
Compatible with Unreal Engine 5.6 Python API
"""

import unreal

print("=" * 60)
print("CREATING MULTIPLAYER LEVEL (FIXED)")
print("=" * 60)

# Get tools
editor_level_lib = unreal.EditorLevelLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()

# Create Maps directory
if not editor_asset_lib.does_directory_exist("/Game/Maps"):
    editor_asset_lib.make_directory("/Game/Maps")
    print("✓ Created /Game/Maps directory")

print("\n--- Adding actors to current level ---")

# Spawn floor
print("  → Spawning floor...")
floor_actor = editor_level_lib.spawn_actor_from_class(
    unreal.StaticMeshActor,
    unreal.Vector(0, 0, 0),
    unreal.Rotator(0, 0, 0)
)

if floor_actor:
    floor_actor.set_actor_scale3d(unreal.Vector(100, 100, 1))
    floor_actor.set_actor_label("Floor")
    print("  ✓ Floor created")

# Spawn Directional Light
print("  → Spawning Directional Light...")
light = editor_level_lib.spawn_actor_from_class(
    unreal.DirectionalLight,
    unreal.Vector(0, 0, 500),
    unreal.Rotator(-45, 0, 0)
)

if light:
    light.set_actor_label("DirectionalLight_Main")
    print("  ✓ Directional Light created")

# Spawn Sky Light
print("  → Spawning Sky Light...")
skylight = editor_level_lib.spawn_actor_from_class(
    unreal.SkyLight,
    unreal.Vector(0, 0, 0),
    unreal.Rotator(0, 0, 0)
)

if skylight:
    skylight.set_actor_label("SkyLight")
    print("  ✓ Sky Light created")

# Spawn 4 Player Starts
print("  → Spawning PlayerStart actors...")
player_starts = [
    (0, 0, 100, "PlayerStart_1"),
    (500, 0, 100, "PlayerStart_2"),
    (0, 500, 100, "PlayerStart_3"),
    (500, 500, 100, "PlayerStart_4")
]

for x, y, z, label in player_starts:
    ps = editor_level_lib.spawn_actor_from_class(
        unreal.PlayerStart,
        unreal.Vector(x, y, z),
        unreal.Rotator(0, 0, 0)
    )
    if ps:
        ps.set_actor_label(label)
        print(f"  ✓ {label} at ({x}, {y}, {z})")

print("\n" + "=" * 60)
print("LEVEL SETUP COMPLETE!")
print("=" * 60)
print("\nNow save the level as MAP_Multiplayer:")
print("  File → Save Current As → MAP_Multiplayer")

