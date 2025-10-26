"""
Unreal Engine Python Script: Create Main Menu Widget Blueprint
Run this script from within the Unreal Editor

This script creates:
- WBP_MainMenu widget blueprint (structure only, visual design must be done manually)
"""

import unreal

# Get asset tools
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
editor_asset_lib = unreal.EditorAssetLibrary()

# Define paths
UI_PATH = "/Game/UI"
MAINMENU_WIDGET_PATH = f"{UI_PATH}/WBP_MainMenu"

print("=" * 60)
print("UI WIDGET CREATION SCRIPT")
print("=" * 60)

# Create UI directory
if not editor_asset_lib.does_directory_exist(UI_PATH):
    editor_asset_lib.make_directory(UI_PATH)
    print(f"✓ Created directory: {UI_PATH}")

# ========================================================================
# CREATE WBP_MainMenu Widget Blueprint
# ========================================================================
print("\n" + "-" * 60)
print("Creating WBP_MainMenu Widget Blueprint...")
print("-" * 60)

if not editor_asset_lib.does_asset_exist(MAINMENU_WIDGET_PATH):
    # Create Widget Blueprint
    widget_factory = unreal.WidgetBlueprintFactory()
    
    widget_bp = asset_tools.create_asset(
        asset_name="WBP_MainMenu",
        package_path=UI_PATH,
        asset_class=unreal.WidgetBlueprint,
        factory=widget_factory
    )
    
    if widget_bp:
        print(f"✓ Created: {MAINMENU_WIDGET_PATH}")
        print("\n⚠ Widget created but needs visual design in UMG Designer:")
        print("\nTo complete the widget, open WBP_MainMenu and add:")
        print("\n1. Canvas Panel (root)")
        print("   └─ Vertical Box (centered)")
        print("       ├─ Text Block: 'Multi Player Test' (title)")
        print("       ├─ Spacer (padding)")
        print("       ├─ Button (Btn_Host) → Text: 'Host Game'")
        print("       ├─ Button (Btn_Join) → Text: 'Join Game'")
        print("       └─ Button (Btn_Quit) → Text: 'Quit Game'")
        print("\n2. In Graph view, add button click events:")
        print("   - Btn_Host OnClicked:")
        print("     → Get Game Instance")
        print("     → Cast to BP_MultiplayerGameInstance")
        print("     → Call CreateSession")
        print("   - Btn_Join OnClicked:")
        print("     → Get Game Instance")
        print("     → Cast to BP_MultiplayerGameInstance")
        print("     → Call FindSessions (or JoinSession)")
        print("   - Btn_Quit OnClicked:")
        print("     → Quit Game")
        
        # Save the widget
        saved = editor_asset_lib.save_asset(MAINMENU_WIDGET_PATH)
        if saved:
            print("\n✓ Widget Blueprint saved")
    else:
        print("✗ Failed to create WBP_MainMenu")
else:
    print(f"✓ Already exists: {MAINMENU_WIDGET_PATH}")

# ========================================================================
# SUMMARY
# ========================================================================
print("\n" + "=" * 60)
print("UI WIDGET CREATION COMPLETE!")
print("=" * 60)

print("\nCreated Widget Blueprint:")
print(f"  ✓ {MAINMENU_WIDGET_PATH}")

print("\n" + "=" * 60)
print("NEXT STEPS - MANUAL UI DESIGN:")
print("=" * 60)
print("\n1. Open WBP_MainMenu in the Widget Blueprint Editor")
print("\n2. Design the visual interface:")
print("   - Add Canvas Panel as root")
print("   - Add Vertical Box in center (use Anchors: Center)")
print("   - Add Text Block for title")
print("   - Add 3 Buttons (Host, Join, Quit)")
print("   - Style buttons as desired")
print("\n3. Add button functionality in Graph:")
print("   - Connect Btn_Host to Game Instance → CreateSession")
print("   - Connect Btn_Join to Game Instance → FindSessions/JoinSession")
print("   - Connect Btn_Quit to Quit Game")
print("\n4. Test the widget:")
print("   - Open MAP_MainMenu")
print("   - Configure Level Blueprint to display widget on BeginPlay")
print("   - Play and test button functionality")

print("\n" + "=" * 60)
print("Refer to BLUEPRINT_CREATION_CHECKLIST.md for detailed steps!")
print("=" * 60)

