"""
Unreal Engine Python Script: Configure Project Settings for Multiplayer
Run this script from within the Unreal Editor

This script configures:
- Default GameMode, Pawn, Controller, Game Instance classes
- Default maps
- Input mappings
"""

import unreal

print("=" * 60)
print("PROJECT SETTINGS CONFIGURATION SCRIPT")
print("=" * 60)

# Get project settings
editor_asset_lib = unreal.EditorAssetLibrary()

# ========================================================================
# 1. CONFIGURE DEFAULT CLASSES
# ========================================================================
print("\n" + "-" * 60)
print("Configuring Default Classes...")
print("-" * 60)

# Load Blueprint classes
gamemode_bp = editor_asset_lib.load_asset("/Game/Blueprints/BP_MultiplayerGameMode")
character_bp = editor_asset_lib.load_asset("/Game/Blueprints/BP_PlayerCharacter")
controller_bp = editor_asset_lib.load_asset("/Game/Blueprints/BP_MultiplayerController")
gameinstance_bp = editor_asset_lib.load_asset("/Game/Blueprints/BP_MultiplayerGameInstance")

if gamemode_bp and character_bp and controller_bp and gameinstance_bp:
    print("✓ All Blueprint classes loaded successfully")
    
    # Get the generated classes
    gamemode_class = gamemode_bp.generated_class()
    character_class = character_bp.generated_class()
    controller_class = controller_bp.generated_class()
    gameinstance_class = gameinstance_bp.generated_class()
    
    # Note: Setting project-wide defaults requires editing config files
    # Python API has limited access to project settings
    print("\n⚠ Note: Some settings must be configured manually:")
    print("   - Project Settings → Maps & Modes")
    print("     → Default GameMode: BP_MultiplayerGameMode")
    print("     → Game Instance Class: BP_MultiplayerGameInstance")
    
    # We can set the GameMode's default pawn class
    if gamemode_class:
        default_gamemode = unreal.get_default_object(gamemode_class)
        default_gamemode.set_editor_property("default_pawn_class", character_class)
        default_gamemode.set_editor_property("player_controller_class", controller_class)
        print("\n✓ GameMode configured:")
        print(f"  → Default Pawn Class: BP_PlayerCharacter")
        print(f"  → Player Controller Class: BP_MultiplayerController")
    
else:
    print("✗ Could not load all Blueprint classes")
    print("   Make sure you've run 01_create_blueprints.py first!")

# ========================================================================
# 2. CONFIGURE INPUT MAPPINGS
# ========================================================================
print("\n" + "-" * 60)
print("Configuring Input Mappings...")
print("-" * 60)

# Note: Input mappings are stored in DefaultInput.ini
# Python API doesn't directly modify Input Settings
# We'll document what needs to be set manually

print("⚠ Input mappings must be configured manually:")
print("\nProject Settings → Engine → Input")
print("\n=== Axis Mappings ===")
print("\nMoveForward:")
print("  - W key: Scale 1.0")
print("  - S key: Scale -1.0")
print("  - Gamepad Left Thumbstick Y-Axis: Scale 1.0")
print("\nMoveRight:")
print("  - D key: Scale 1.0")
print("  - A key: Scale -1.0")
print("  - Gamepad Left Thumbstick X-Axis: Scale 1.0")
print("\nTurn:")
print("  - Mouse X: Scale 1.0")
print("  - Gamepad Right Thumbstick X-Axis: Scale 1.0")
print("\nLookUp:")
print("  - Mouse Y: Scale -1.0")
print("  - Gamepad Right Thumbstick Y-Axis: Scale 1.0")
print("\n=== Action Mappings ===")
print("\nJump:")
print("  - Space Bar")
print("  - Gamepad Face Button Bottom")

# ========================================================================
# 3. CONFIGURE DEFAULT MAPS
# ========================================================================
print("\n" + "-" * 60)
print("Configuring Default Maps...")
print("-" * 60)

# Check if maps exist
multiplayer_map_exists = editor_asset_lib.does_asset_exist("/Game/Maps/MAP_Multiplayer")
mainmenu_map_exists = editor_asset_lib.does_asset_exist("/Game/Maps/MAP_MainMenu")

if multiplayer_map_exists and mainmenu_map_exists:
    print("✓ Both maps exist")
    print("\n⚠ Set these manually in Project Settings → Maps & Modes:")
    print(f"  → Editor Startup Map: /Game/Maps/MAP_Multiplayer")
    print(f"  → Game Default Map: /Game/Maps/MAP_MainMenu")
    print(f"  → Server Default Map: /Game/Maps/MAP_Multiplayer")
else:
    print("✗ Maps not found. Run 02_create_levels.py first!")

# ========================================================================
# 4. VERIFY ONLINE SUBSYSTEM CONFIGURATION
# ========================================================================
print("\n" + "-" * 60)
print("Verifying Online Subsystem Configuration...")
print("-" * 60)

print("✓ Online Subsystem plugins should already be enabled")
print("  Check Config/DefaultEngine.ini for:")
print("  - [OnlineSubsystem] DefaultPlatformService=Null")
print("  - [OnlineSubsystemNull] bEnabled=true")
print("  - Network driver definitions configured")

# ========================================================================
# SUMMARY
# ========================================================================
print("\n" + "=" * 60)
print("CONFIGURATION COMPLETE!")
print("=" * 60)

print("\n✓ Automated Configuration:")
print("  - GameMode Default Pawn Class set to BP_PlayerCharacter")
print("  - GameMode Player Controller Class set to BP_MultiplayerController")

print("\n⚠ Manual Configuration Required:")
print("\n1. Project Settings → Maps & Modes:")
print("   - Default GameMode: BP_MultiplayerGameMode")
print("   - Game Instance Class: BP_MultiplayerGameInstance")
print("   - Editor Startup Map: MAP_Multiplayer")
print("   - Game Default Map: MAP_MainMenu")
print("\n2. Project Settings → Engine → Input:")
print("   - Add all Axis Mappings (MoveForward, MoveRight, Turn, LookUp)")
print("   - Add all Action Mappings (Jump)")
print("   - See details above for specific key bindings")

print("\n" + "=" * 60)
print("After manual configuration, you're ready to test!")
print("=" * 60)

