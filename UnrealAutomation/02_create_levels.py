"""
Unreal Engine Python Script: Create Game Levels
Run this script from within the Unreal Editor

This script creates:
- MAP_Multiplayer (main gameplay level with floor, lighting, PlayerStarts)
- MAP_MainMenu (menu level)
"""

import unreal

# Get necessary subsystems
editor_level_lib = unreal.EditorLevelLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()
level_editor_subsystem = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)

# Define paths
MAPS_PATH = "/Game/Maps"
MULTIPLAYER_MAP_PATH = f"{MAPS_PATH}/MAP_Multiplayer"
MAINMENU_MAP_PATH = f"{MAPS_PATH}/MAP_MainMenu"

print("=" * 60)
print("MULTIPLAYER LEVEL CREATION SCRIPT")
print("=" * 60)

# Create Maps directory
if not editor_asset_lib.does_directory_exist(MAPS_PATH):
    editor_asset_lib.make_directory(MAPS_PATH)
    print(f"✓ Created directory: {MAPS_PATH}")

# ========================================================================
# 1. CREATE MAP_Multiplayer
# ========================================================================
print("\n" + "-" * 60)
print("Creating MAP_Multiplayer...")
print("-" * 60)

# Create new level
new_level = unreal.EditorLevelUtils.new_level(MULTIPLAYER_MAP_PATH)

if new_level:
    print(f"✓ Created level: {MULTIPLAYER_MAP_PATH}")
    
    # Add floor plane
    print("  → Adding floor...")
    floor_location = unreal.Vector(0, 0, 0)
    floor_rotation = unreal.Rotator(0, 0, 0)
    floor_scale = unreal.Vector(100, 100, 1)
    
    floor_actor = editor_level_lib.spawn_actor_from_class(
        unreal.StaticMeshActor,
        floor_location,
        floor_rotation
    )
    
    if floor_actor:
        floor_actor.set_actor_scale3d(floor_scale)
        floor_actor.set_actor_label("Floor")
        
        # Set floor to use a basic cube mesh
        static_mesh_component = floor_actor.static_mesh_component
        cube_mesh = unreal.EditorAssetLibrary.load_asset("/Engine/BasicShapes/Cube")
        if cube_mesh:
            static_mesh_component.set_static_mesh(cube_mesh)
        
        print("    ✓ Floor created at (0, 0, 0) with scale (100, 100, 1)")
    
    # Add Directional Light
    print("  → Adding Directional Light...")
    light_location = unreal.Vector(0, 0, 500)
    light_rotation = unreal.Rotator(-45, 0, 0)
    
    directional_light = editor_level_lib.spawn_actor_from_class(
        unreal.DirectionalLight,
        light_location,
        light_rotation
    )
    
    if directional_light:
        directional_light.set_actor_label("DirectionalLight_Main")
        print("    ✓ Directional Light created")
    
    # Add Sky Light
    print("  → Adding Sky Light...")
    skylight = editor_level_lib.spawn_actor_from_class(
        unreal.SkyLight,
        unreal.Vector(0, 0, 0),
        unreal.Rotator(0, 0, 0)
    )
    
    if skylight:
        skylight.set_actor_label("SkyLight")
        print("    ✓ Sky Light created")
    
    # Add Sky Atmosphere
    print("  → Adding Sky Atmosphere...")
    sky_atmosphere = editor_level_lib.spawn_actor_from_class(
        unreal.SkyAtmosphere,
        unreal.Vector(0, 0, 0),
        unreal.Rotator(0, 0, 0)
    )
    
    if sky_atmosphere:
        sky_atmosphere.set_actor_label("SkyAtmosphere")
        print("    ✓ Sky Atmosphere created")
    
    # Add PlayerStart actors (4 of them for multiplayer)
    print("  → Adding PlayerStart actors...")
    player_start_positions = [
        (0, 0, 100, "PlayerStart_1"),
        (500, 0, 100, "PlayerStart_2"),
        (0, 500, 100, "PlayerStart_3"),
        (500, 500, 100, "PlayerStart_4")
    ]
    
    for x, y, z, label in player_start_positions:
        player_start = editor_level_lib.spawn_actor_from_class(
            unreal.PlayerStart,
            unreal.Vector(x, y, z),
            unreal.Rotator(0, 0, 0)
        )
        
        if player_start:
            player_start.set_actor_label(label)
            print(f"    ✓ {label} at ({x}, {y}, {z})")
    
    # Add Nav Mesh Bounds Volume
    print("  → Adding Nav Mesh Bounds Volume...")
    navmesh_location = unreal.Vector(250, 250, 0)
    navmesh_scale = unreal.Vector(50, 50, 10)
    
    navmesh_bounds = editor_level_lib.spawn_actor_from_class(
        unreal.NavMeshBoundsVolume,
        navmesh_location,
        unreal.Rotator(0, 0, 0)
    )
    
    if navmesh_bounds:
        navmesh_bounds.set_actor_scale3d(navmesh_scale)
        navmesh_bounds.set_actor_label("NavMeshBoundsVolume")
        print("    ✓ Nav Mesh Bounds Volume created")
    
    # Save the level
    print("  → Saving level...")
    saved = editor_asset_lib.save_asset(MULTIPLAYER_MAP_PATH)
    if saved:
        print("    ✓ Level saved successfully")
    
    print(f"\n✓ MAP_Multiplayer created successfully!")

else:
    print("✗ Failed to create MAP_Multiplayer")

# ========================================================================
# 2. CREATE MAP_MainMenu
# ========================================================================
print("\n" + "-" * 60)
print("Creating MAP_MainMenu...")
print("-" * 60)

# Create new level for main menu
menu_level = unreal.EditorLevelUtils.new_level(MAINMENU_MAP_PATH)

if menu_level:
    print(f"✓ Created level: {MAINMENU_MAP_PATH}")
    
    # Add basic lighting for background
    print("  → Adding basic lighting...")
    light_location = unreal.Vector(0, 0, 300)
    light_rotation = unreal.Rotator(-45, 0, 0)
    
    menu_light = editor_level_lib.spawn_actor_from_class(
        unreal.DirectionalLight,
        light_location,
        light_rotation
    )
    
    if menu_light:
        menu_light.set_actor_label("MenuLight")
        print("    ✓ Directional Light created")
    
    # Add Sky Atmosphere for nice background
    sky_atmos = editor_level_lib.spawn_actor_from_class(
        unreal.SkyAtmosphere,
        unreal.Vector(0, 0, 0),
        unreal.Rotator(0, 0, 0)
    )
    
    if sky_atmos:
        sky_atmos.set_actor_label("SkyAtmosphere_Menu")
        print("    ✓ Sky Atmosphere created")
    
    # Note: Level Blueprint widget setup must be done manually
    print("  → Manual config needed: Open Level Blueprint")
    print("    - Add Event BeginPlay")
    print("    - Create Widget (WBP_MainMenu)")
    print("    - Add to Viewport")
    print("    - Set Show Mouse Cursor = True")
    print("    - Set Input Mode UI Only")
    
    # Save the level
    print("  → Saving level...")
    saved = editor_asset_lib.save_asset(MAINMENU_MAP_PATH)
    if saved:
        print("    ✓ Level saved successfully")
    
    print(f"\n✓ MAP_MainMenu created successfully!")

else:
    print("✗ Failed to create MAP_MainMenu")

# ========================================================================
# SUMMARY
# ========================================================================
print("\n" + "=" * 60)
print("LEVEL CREATION COMPLETE!")
print("=" * 60)
print("\nCreated Levels:")
print(f"  ✓ {MULTIPLAYER_MAP_PATH}")
print(f"    - Floor (10,000 x 10,000 units)")
print(f"    - Directional Light, Sky Light, Sky Atmosphere")
print(f"    - 4 PlayerStart actors at different positions")
print(f"    - Nav Mesh Bounds Volume")
print(f"\n  ✓ {MAINMENU_MAP_PATH}")
print(f"    - Basic lighting and atmosphere")
print(f"    - Ready for UI widget display")

print("\n" + "=" * 60)
print("NEXT STEPS:")
print("=" * 60)
print("\n1. Open MAP_MainMenu:")
print("   - Blueprints → Open Level Blueprint")
print("   - Configure widget display (see manual steps above)")
print("\n2. Test MAP_Multiplayer:")
print("   - Open the level")
print("   - Press Play to test")
print("   - Verify all 4 PlayerStarts are visible")
print("\n3. Configure Project Settings:")
print("   - Set Editor Startup Map to MAP_Multiplayer")
print("   - Set Game Default Map to MAP_MainMenu")

print("\n" + "=" * 60)

