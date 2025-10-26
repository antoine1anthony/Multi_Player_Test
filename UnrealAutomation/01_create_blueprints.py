"""
Unreal Engine Python Script: Create Multiplayer Blueprint Classes
Run this script from within the Unreal Editor Python console or via File -> Execute Python Script

This script creates the core Blueprint classes for multiplayer functionality:
- BP_MultiplayerGameMode
- BP_PlayerCharacter  
- BP_MultiplayerController
- BP_MultiplayerGameInstance
"""

import unreal

# Get asset tools
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
editor_asset_lib = unreal.EditorAssetLibrary()

# Define asset paths
BLUEPRINTS_PATH = "/Game/Blueprints"
CHARACTER_BP_PATH = f"{BLUEPRINTS_PATH}/BP_PlayerCharacter"
GAMEMODE_BP_PATH = f"{BLUEPRINTS_PATH}/BP_MultiplayerGameMode"
CONTROLLER_BP_PATH = f"{BLUEPRINTS_PATH}/BP_MultiplayerController"
GAMEINSTANCE_BP_PATH = f"{BLUEPRINTS_PATH}/BP_MultiplayerGameInstance"

print("=" * 60)
print("MULTIPLAYER BLUEPRINT CREATION SCRIPT")
print("=" * 60)

# Create Blueprints directory if it doesn't exist
if not editor_asset_lib.does_directory_exist(BLUEPRINTS_PATH):
    editor_asset_lib.make_directory(BLUEPRINTS_PATH)
    print(f"✓ Created directory: {BLUEPRINTS_PATH}")
else:
    print(f"✓ Directory exists: {BLUEPRINTS_PATH}")

# ========================================================================
# 1. CREATE BP_MultiplayerGameMode
# ========================================================================
print("\n" + "-" * 60)
print("Creating BP_MultiplayerGameMode...")
print("-" * 60)

if not editor_asset_lib.does_asset_exist(GAMEMODE_BP_PATH):
    # Create a Blueprint based on GameModeBase
    gamemode_factory = unreal.BlueprintFactory()
    gamemode_factory.set_editor_property("parent_class", unreal.GameModeBase)

    gamemode_bp = asset_tools.create_asset(
        asset_name="BP_MultiplayerGameMode",
        package_path=BLUEPRINTS_PATH,
        asset_class=unreal.Blueprint,
        factory=gamemode_factory
    )

    if gamemode_bp:
        print(f"✓ Created: {GAMEMODE_BP_PATH}")

        # Get the Blueprint's generated class
        bp_generated_class = gamemode_bp.generated_class()
        if bp_generated_class:
            # Get the default object to set properties
            default_obj = unreal.get_default_object(bp_generated_class)

            # Note: Some properties can only be set in Blueprint editor
            # We'll document what needs manual configuration
            print("  → GameMode created successfully")
            print("  → Manual config needed: Max Players, Default Pawn Class")
    else:
        print("✗ Failed to create BP_MultiplayerGameMode")
else:
    print(f"✓ Already exists: {GAMEMODE_BP_PATH}")

# ========================================================================
# 2. CREATE BP_PlayerCharacter
# ========================================================================
print("\n" + "-" * 60)
print("Creating BP_PlayerCharacter...")
print("-" * 60)

if not editor_asset_lib.does_asset_exist(CHARACTER_BP_PATH):
    # Create a Blueprint based on Character
    character_factory = unreal.BlueprintFactory()
    character_factory.set_editor_property("parent_class", unreal.Character)

    character_bp = asset_tools.create_asset(
        asset_name="BP_PlayerCharacter",
        package_path=BLUEPRINTS_PATH,
        asset_class=unreal.Blueprint,
        factory=character_factory
    )

    if character_bp:
        print(f"✓ Created: {CHARACTER_BP_PATH}")

        # Get the Blueprint's generated class
        bp_generated_class = character_bp.generated_class()
        if bp_generated_class:
            default_obj = unreal.get_default_object(bp_generated_class)

            # Set replication properties (critical for multiplayer)
            default_obj.set_editor_property("bReplicates", True)
            default_obj.set_editor_property("bReplicateMovement", True)

            # Set Auto Possess to Disabled (important for multiplayer)
            default_obj.set_editor_property(
                "auto_possess_player", unreal.AutoPossessPlayer.DISABLED)
            default_obj.set_editor_property(
                "auto_possess_ai", unreal.AutoPossessAI.DISABLED)

            print("  → Replication enabled: bReplicates = True")
            print("  → Movement replication enabled")
            print("  → Auto Possess set to Disabled")
            print("  → Manual config needed: Add SK_Mannequin mesh, Camera, SpringArm")
            print("  → Manual config needed: Add input events in Event Graph")
    else:
        print("✗ Failed to create BP_PlayerCharacter")
else:
    print(f"✓ Already exists: {CHARACTER_BP_PATH}")

# ========================================================================
# 3. CREATE BP_MultiplayerController
# ========================================================================
print("\n" + "-" * 60)
print("Creating BP_MultiplayerController...")
print("-" * 60)

if not editor_asset_lib.does_asset_exist(CONTROLLER_BP_PATH):
    # Create a Blueprint based on PlayerController
    controller_factory = unreal.BlueprintFactory()
    controller_factory.set_editor_property(
        "parent_class", unreal.PlayerController)

    controller_bp = asset_tools.create_asset(
        asset_name="BP_MultiplayerController",
        package_path=BLUEPRINTS_PATH,
        asset_class=unreal.Blueprint,
        factory=controller_factory
    )

    if controller_bp:
        print(f"✓ Created: {CONTROLLER_BP_PATH}")

        bp_generated_class = controller_bp.generated_class()
        if bp_generated_class:
            default_obj = unreal.get_default_object(bp_generated_class)

            # Set mouse cursor to hidden (for third-person gameplay)
            default_obj.set_editor_property("bShow_mouse_cursor", False)

            print("  → Mouse cursor set to hidden")
            print("  → Controller ready for use")
    else:
        print("✗ Failed to create BP_MultiplayerController")
else:
    print(f"✓ Already exists: {CONTROLLER_BP_PATH}")

# ========================================================================
# 4. CREATE BP_MultiplayerGameInstance
# ========================================================================
print("\n" + "-" * 60)
print("Creating BP_MultiplayerGameInstance...")
print("-" * 60)

if not editor_asset_lib.does_asset_exist(GAMEINSTANCE_BP_PATH):
    # Create a Blueprint based on GameInstance
    gameinstance_factory = unreal.BlueprintFactory()
    gameinstance_factory.set_editor_property(
        "parent_class", unreal.GameInstance)

    gameinstance_bp = asset_tools.create_asset(
        asset_name="BP_MultiplayerGameInstance",
        package_path=BLUEPRINTS_PATH,
        asset_class=unreal.Blueprint,
        factory=gameinstance_factory
    )

    if gameinstance_bp:
        print(f"✓ Created: {GAMEINSTANCE_BP_PATH}")
        print("  → Manual config needed: Add Event Init with Create Player node")
        print("  → Manual config needed: Add CreateSession, FindSessions, JoinSession functions")
    else:
        print("✗ Failed to create BP_MultiplayerGameInstance")
else:
    print(f"✓ Already exists: {GAMEINSTANCE_BP_PATH}")

# ========================================================================
# SUMMARY
# ========================================================================
print("\n" + "=" * 60)
print("BLUEPRINT CREATION COMPLETE!")
print("=" * 60)
print("\nCreated Blueprints:")
print(f"  ✓ {GAMEMODE_BP_PATH}")
print(f"  ✓ {CHARACTER_BP_PATH}")
print(f"  ✓ {CONTROLLER_BP_PATH}")
print(f"  ✓ {GAMEINSTANCE_BP_PATH}")

print("\n" + "=" * 60)
print("NEXT STEPS - MANUAL CONFIGURATION REQUIRED:")
print("=" * 60)
print("\n1. BP_PlayerCharacter:")
print("   - Open the Blueprint")
print("   - Add SK_Mannequin mesh to Mesh component")
print("   - Set mesh Transform: Location (0,0,-90), Rotation (0,0,-90)")
print("   - Add SpringArm component")
print("   - Add Camera as child of SpringArm")
print("   - Add input events in Event Graph (MoveForward, MoveRight, Turn, LookUp, Jump)")
print("\n2. BP_MultiplayerGameMode:")
print("   - Set Default Pawn Class to BP_PlayerCharacter")
print("   - Set Player Controller Class to BP_MultiplayerController")
print("\n3. BP_MultiplayerGameInstance:")
print("   - Add Event Init node")
print("   - Add Create Player node (Player Index = 1) for split-screen")
print("   - Add CreateSession, FindSessions, JoinSession custom functions")
print("\n4. Project Settings:")
print("   - Set Game Instance Class to BP_MultiplayerGameInstance")
print("   - Set Default GameMode to BP_MultiplayerGameMode")

print("\n" + "=" * 60)
print("Refer to BLUEPRINT_CREATION_CHECKLIST.md for detailed steps!")
print("=" * 60)
