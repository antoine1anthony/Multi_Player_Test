"""
FIXED VERSION - Creates Multiplayer Blueprint Classes
Compatible with Unreal Engine 5.6 Python API
"""

import unreal

print("=" * 60)
print("CREATING MULTIPLAYER BLUEPRINTS (FIXED)")
print("=" * 60)

# Get necessary tools
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
editor_asset_lib = unreal.EditorAssetLibrary()

# Create Blueprints directory
if not editor_asset_lib.does_directory_exist("/Game/Blueprints"):
    editor_asset_lib.make_directory("/Game/Blueprints")
    print("✓ Created /Game/Blueprints directory")

# 1. CREATE BP_MultiplayerGameMode
print("\n--- Creating BP_MultiplayerGameMode ---")
factory = unreal.BlueprintFactory()
factory.set_editor_property("parent_class", unreal.GameModeBase)

gamemode_bp = asset_tools.create_asset(
    "BP_MultiplayerGameMode",
    "/Game/Blueprints",
    unreal.Blueprint,
    factory
)

if gamemode_bp:
    print("✓ BP_MultiplayerGameMode created")
    editor_asset_lib.save_asset("/Game/Blueprints/BP_MultiplayerGameMode")
else:
    print("✗ Failed to create BP_MultiplayerGameMode")

# 2. CREATE BP_PlayerCharacter
print("\n--- Creating BP_PlayerCharacter ---")
factory = unreal.BlueprintFactory()
factory.set_editor_property("parent_class", unreal.Character)

character_bp = asset_tools.create_asset(
    "BP_PlayerCharacter",
    "/Game/Blueprints",
    unreal.Blueprint,
    factory
)

if character_bp:
    print("✓ BP_PlayerCharacter created")

    # Set replication
    bp_class = character_bp.generated_class()
    if bp_class:
        default_obj = unreal.get_default_object(bp_class)
        default_obj.set_editor_property("b_replicates", True)
        default_obj.set_editor_property("b_replicate_movement", True)
        print("  ✓ Replication enabled")

    editor_asset_lib.save_asset("/Game/Blueprints/BP_PlayerCharacter")
else:
    print("✗ Failed to create BP_PlayerCharacter")

# 3. CREATE BP_MultiplayerController
print("\n--- Creating BP_MultiplayerController ---")
factory = unreal.BlueprintFactory()
factory.set_editor_property("parent_class", unreal.PlayerController)

controller_bp = asset_tools.create_asset(
    "BP_MultiplayerController",
    "/Game/Blueprints",
    unreal.Blueprint,
    factory
)

if controller_bp:
    print("✓ BP_MultiplayerController created")
    editor_asset_lib.save_asset("/Game/Blueprints/BP_MultiplayerController")
else:
    print("✗ Failed to create BP_MultiplayerController")

# 4. CREATE BP_MultiplayerGameInstance
print("\n--- Creating BP_MultiplayerGameInstance ---")
factory = unreal.BlueprintFactory()
factory.set_editor_property("parent_class", unreal.GameInstance)

gameinstance_bp = asset_tools.create_asset(
    "BP_MultiplayerGameInstance",
    "/Game/Blueprints",
    unreal.Blueprint,
    factory
)

if gameinstance_bp:
    print("✓ BP_MultiplayerGameInstance created")
    editor_asset_lib.save_asset("/Game/Blueprints/BP_MultiplayerGameInstance")
else:
    print("✗ Failed to create BP_MultiplayerGameInstance")

print("\n" + "=" * 60)
print("BLUEPRINT CREATION COMPLETE!")
print("=" * 60)
print("\nCheck Content/Blueprints folder in Content Browser")
