"""
Create Remaining Multiplayer Blueprints
Run this in Unreal Editor to complete the Blueprint setup
"""

import unreal

print("=" * 60)
print("CREATING REMAINING MULTIPLAYER BLUEPRINTS")
print("=" * 60)

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
editor_asset_lib = unreal.EditorAssetLibrary()

# Ensure Blueprints directory exists
if not editor_asset_lib.does_directory_exist("/Game/Blueprints"):
    editor_asset_lib.make_directory("/Game/Blueprints")

# 1. CREATE BP_PlayerCharacter (if not exists)
print("\n--- Checking BP_PlayerCharacter ---")
if not editor_asset_lib.does_asset_exist("/Game/Blueprints/BP_PlayerCharacter"):
    print("Creating BP_PlayerCharacter...")
    factory = unreal.BlueprintFactory()
    factory.set_editor_property("parent_class", unreal.Character)

    character_bp = asset_tools.create_asset(
        "BP_PlayerCharacter",
        "/Game/Blueprints",
        unreal.Blueprint,
        factory
    )

    if character_bp:
        bp_class = character_bp.generated_class()
        if bp_class:
            default_obj = unreal.get_default_object(bp_class)
            default_obj.set_editor_property("b_replicates", True)
            default_obj.set_editor_property("b_replicate_movement", True)
            print("✓ BP_PlayerCharacter created with replication enabled")
        editor_asset_lib.save_asset("/Game/Blueprints/BP_PlayerCharacter")
else:
    print("✓ BP_PlayerCharacter already exists")

# 2. CREATE BP_MultiplayerController
print("\n--- Creating BP_MultiplayerController ---")
if not editor_asset_lib.does_asset_exist("/Game/Blueprints/BP_MultiplayerController"):
    factory = unreal.BlueprintFactory()
    factory.set_editor_property("parent_class", unreal.PlayerController)

    controller_bp = asset_tools.create_asset(
        "BP_MultiplayerController",
        "/Game/Blueprints",
        unreal.Blueprint,
        factory
    )

    if controller_bp:
        bp_class = controller_bp.generated_class()
        if bp_class:
            default_obj = unreal.get_default_object(bp_class)
            default_obj.set_editor_property("b_show_mouse_cursor", False)
        print("✓ BP_MultiplayerController created")
        editor_asset_lib.save_asset(
            "/Game/Blueprints/BP_MultiplayerController")
else:
    print("✓ BP_MultiplayerController already exists")

# 3. CREATE BP_MultiplayerGameInstance
print("\n--- Creating BP_MultiplayerGameInstance ---")
if not editor_asset_lib.does_asset_exist("/Game/Blueprints/BP_MultiplayerGameInstance"):
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
        editor_asset_lib.save_asset(
            "/Game/Blueprints/BP_MultiplayerGameInstance")
else:
    print("✓ BP_MultiplayerGameInstance already exists")

print("\n" + "=" * 60)
print("ALL BLUEPRINT CLASSES CREATED!")
print("=" * 60)
print("\nNext steps:")
print("1. Open BP_PlayerCharacter and add:")
print("   - SK_Mannequin skeletal mesh")
print("   - SpringArm component")
print("   - Camera component")
print("   - Input events")
print("\n2. Open BP_MultiplayerGameInstance and add:")
print("   - Event Init with Create Player node (Index=1)")
print("   - CreateSession, FindSessions, JoinSession functions")
print("\n3. Configure Project Settings:")
print("   - Set Default GameMode to BP_MultiplayerGameMode")
print("   - Set Game Instance to BP_MultiplayerGameInstance")
print("   - Set Default Pawn to BP_PlayerCharacter")
print("   - Set Default Controller to BP_MultiplayerController")

