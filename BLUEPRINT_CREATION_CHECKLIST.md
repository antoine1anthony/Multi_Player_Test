# Blueprint Creation Checklist
## Quick Reference for Multi_Player_Test Implementation

Based on Unreal Engine multiplayer best practices from professional game development resources.

---

## ✅ Phase 1: Get Mannequin Assets

### Option 1: Epic Games Launcher (EASIEST)
- [ ] Open **Epic Games Launcher**
- [ ] Go to **Unreal Engine** tab → **Library**
- [ ] Scroll to **Vault** section
- [ ] Click **Add to Project**
- [ ] Search: **"UE5 Starter Content"** or **"Third Person"**
- [ ] Select **Multi_Player_Test** project
- [ ] Click **Add to Project**
- [ ] Wait for download/installation
- [ ] Restart Unreal Editor

### Option 2: Migrate from Template Project
- [ ] Launch UE 5.6 from Epic Launcher
- [ ] Create **New Project** → **Games** → **Third Person**
- [ ] Name: `TempMannequin`
- [ ] Open the temp project
- [ ] Content Browser → Navigate to `Content/Characters/`
- [ ] Right-click **Characters** folder
- [ ] Select **Asset Actions** → **Migrate**
- [ ] Browse to your `Multi_Player_Test/Content/` folder
- [ ] Click **Select Folder** → **OK**
- [ ] Close temp project
- [ ] Open Multi_Player_Test → Verify assets in Content/Characters/

**Verification:**
- [ ] Content Browser has `Content/Characters/Mannequins/` folder
- [ ] Contains: `SK_Mannequin` skeletal mesh
- [ ] Contains: `ABP_Mannequin` animation blueprint

---

## ✅ Phase 2: Create Game Mode Blueprint

### BP_MultiplayerGameMode

**Creation:**
- [ ] Content Browser → Right-click in empty space
- [ ] **Blueprint Class**
- [ ] **All Classes** → Search: "Game Mode Base"
- [ ] Select **Game Mode Base** → Click **Select**
- [ ] Name: `BP_MultiplayerGameMode`
- [ ] Press Enter

**Configuration:**
- [ ] Double-click `BP_MultiplayerGameMode` to open
- [ ] Click **Class Defaults** button (top toolbar, looks like a list icon)
- [ ] In **Details** panel (right side):

**Classes Section:**
- [ ] **Default Pawn Class**: None (will set later)
- [ ] **Player Controller Class**: None (will set later)
- [ ] **Player State Class**: PlayerState (default)
- [ ] **Game State Class**: GameStateBase (default)

**Game Mode Section:**
- [ ] Find "Game" category
- [ ] **Number of Players**: `4`

**Save:**
- [ ] Click **Compile** (green checkmark)
- [ ] Click **Save** (floppy disk icon)
- [ ] Close Blueprint Editor

---

## ✅ Phase 3: Create Player Character Blueprint

### BP_PlayerCharacter

**Creation:**
- [ ] Content Browser → Right-click
- [ ] **Blueprint Class**
- [ ] Select **Character** (should be at top)
- [ ] Name: `BP_PlayerCharacter`

**Open and Configure Components:**
- [ ] Double-click to open Blueprint Editor
- [ ] Switch to **Viewport** tab (top-left tabs)

### Configure Mesh Component:

- [ ] In **Components** panel (left), select **Mesh (Inherited)**
- [ ] In **Details** panel (right):

**Mesh Section:**
- [ ] **Skeletal Mesh Asset**: Click dropdown → Select `SK_Mannequin`
  - If not found, search "mannequin" or "manny"
- [ ] **Anim Class**: Select `ABP_Mannequin` (or Animation Blueprint from Characters folder)

**Transform Section:**
- [ ] **Location**: 
  - X: `0.0`
  - Y: `0.0`
  - Z: `-90.0` ⚠️ Important!
- [ ] **Rotation**:
  - X: `0.0`
  - Y: `0.0`
  - Z: `-90.0` ⚠️ Important!
- [ ] **Scale**: 
  - X: `1.0`
  - Y: `1.0`
  - Z: `1.0`

**Why -90 rotation?** The mannequin model faces Y+ axis by default, but Character class expects forward to be X+ axis.

### Add Camera System:

- [ ] Click **Add** button (top-left of Components panel)
- [ ] Search: "Spring Arm"
- [ ] Click **Spring Arm Component** to add it
- [ ] Drag **SpringArm** component onto **Mesh** in hierarchy to attach it

**Configure Spring Arm:**
- [ ] Select **SpringArm** component
- [ ] In **Details**:

**Transform:**
- [ ] **Location**: 
  - X: `0.0`
  - Y: `0.0`
  - Z: `90.0` (shoulder height)

**Camera Settings:**
- [ ] **Target Arm Length**: `400.0`
- [ ] **Socket Offset**: X: `0`, Y: `0`, Z: `0`
- [ ] **Use Pawn Control Rotation**: ✅ **Checked**
- [ ] **Inherit Pitch**: ✅ **Checked**
- [ ] **Inherit Yaw**: ✅ **Checked**
- [ ] **Inherit Roll**: ✅ **Checked**

**Add Camera:**
- [ ] Click **Add** button
- [ ] Search: "Camera"
- [ ] Click **Camera Component**
- [ ] Drag **Camera** onto **SpringArm** to make it a child

**Configure Camera:**
- [ ] Select **Camera** component
- [ ] No changes needed (defaults are fine)

### Configure Character Movement:

- [ ] Select **CharacterMovement (Inherited)** component
- [ ] In **Details**:

**Character Movement: Walking:**
- [ ] **Max Walk Speed**: `600.0`
- [ ] **Ground Friction**: `8.0`
- [ ] **Max Acceleration**: `2048.0`

**Character Movement: Jumping / Falling:**
- [ ] **Jump Z Velocity**: `600.0`
- [ ] **Air Control**: `0.2`

### Configure Replication (CRITICAL for multiplayer):

- [ ] Click **Class Defaults** button (toolbar)
- [ ] In **Details** panel, find sections:

**Replication Section:**
- [ ] **Replicates**: ✅ **Checked** ⚠️ MUST BE CHECKED
- [ ] **Replicate Movement**: ✅ **Checked** ⚠️ MUST BE CHECKED

**Pawn Section:**
- [ ] **Auto Possess Player**: **Disabled** ⚠️ Important for multiplayer!
- [ ] **Auto Possess AI**: **Disabled**

**Camera Section:**
- [ ] **Use Controller Rotation Pitch**: ❌ Unchecked
- [ ] **Use Controller Rotation Yaw**: ❌ Unchecked
- [ ] **Use Controller Rotation Roll**: ❌ Unchecked
- [ ] **Orient Rotation to Movement**: ✅ Checked
- [ ] **Rotation Rate**: Yaw: `540.0`

### Add Input Events:

- [ ] Switch to **Event Graph** tab
- [ ] Delete any default nodes you don't need

**Add Movement Forward/Backward:**
- [ ] Right-click in graph → Search: "InputAxis MoveForward"
- [ ] Click to add **InputAxis MoveForward** event node
- [ ] From execution pin, drag out → Search: "Add Movement Input"
- [ ] Add **Add Movement Input** node

**Configure Forward Movement:**
- [ ] From **Add Movement Input** node, right-click **World Direction** pin
- [ ] Search: "Get Control Rotation"
- [ ] From **Get Control Rotation** return value, drag out
- [ ] Search: "Get Forward Vector"
- [ ] Connect **Return Value** to **World Direction**
- [ ] Connect **Axis Value** from InputAxis to **Scale Value** pin

**Add Movement Left/Right:**
- [ ] Right-click → "InputAxis MoveRight"
- [ ] From execution, **Add Movement Input** node
- [ ] Get Control Rotation → **Get Right Vector**
- [ ] Connect to **World Direction**
- [ ] Connect **Axis Value** to **Scale Value**

**Add Look Up/Down:**
- [ ] Right-click → "InputAxis LookUp"
- [ ] From execution → "Add Controller Pitch Input"
- [ ] Connect **Axis Value** to **Pitch Value**

**Add Look Left/Right (Turn):**
- [ ] Right-click → "InputAxis Turn"
- [ ] From execution → "Add Controller Yaw Input"
- [ ] Connect **Axis Value** to **Yaw Value**

**Add Jump:**
- [ ] Right-click → "InputAction Jump"
- [ ] From **Pressed** pin → "Jump" node
- [ ] From **Released** pin → "Stop Jumping" node

**Save:**
- [ ] **Compile**
- [ ] **Save**
- [ ] Close

---

## ✅ Phase 4: Create Player Controller Blueprint

### BP_MultiplayerController

**Creation:**
- [ ] Content Browser → Right-click
- [ ] **Blueprint Class**
- [ ] **All Classes** → Search: "Player Controller"
- [ ] Select **Player Controller** → Name: `BP_MultiplayerController`

**Configuration:**
- [ ] Double-click to open
- [ ] Click **Class Defaults**
- [ ] In **Details**:

**Mouse Interface:**
- [ ] **Show Mouse Cursor**: ❌ Unchecked (for third-person)
- [ ] **Enable Click Events**: ❌ Unchecked
- [ ] **Enable Mouse Over Events**: ❌ Unchecked

**Input:**
- [ ] **Enable Input**: ✅ Checked

**Save:**
- [ ] **Compile** → **Save** → Close

---

## ✅ Phase 5: Create Game Instance Blueprint

### BP_MultiplayerGameInstance

**Creation:**
- [ ] Content Browser → Right-click
- [ ] **Blueprint Class**
- [ ] **All Classes** → Search: "Game Instance"
- [ ] Select **Game Instance** → Name: `BP_MultiplayerGameInstance`

**Add Split-Screen Support:**
- [ ] Open Blueprint
- [ ] Go to **Event Graph**
- [ ] Find or create **Event Init** node

**Create Player 2 (for local split-screen):**
- [ ] From **Event Init** execution pin
- [ ] Search: "Create Player"
- [ ] Add **Create Player** node
- [ ] **Player Index**: `1` (this creates Player 2)
- [ ] **Spawn Pawn If Necessary**: ✅ Checked

**Add Custom Functions for Online Multiplayer:**

### Function: CreateSession

- [ ] Click **+ Function** button (left panel)
- [ ] Name: `CreateSession`
- [ ] In function graph:
  - [ ] Add **Create Session** node
  - [ ] **Public Connections**: `4`
  - [ ] **Use LAN**: ✅ Checked (for local testing)
  - [ ] **Session Name**: Type `"GameSession"`
  - [ ] From **On Success** pin: Add **Open Level** node
    - [ ] **Level Name**: `"MAP_Multiplayer"`
    - [ ] **Options**: `"?listen"` (makes it a listen server)
  - [ ] From **On Failure** pin: Add **Print String** (optional, for debugging)

### Function: FindSessions

- [ ] Click **+ Function**
- [ ] Name: `FindSessions`
- [ ] Add **Find Sessions** node
  - [ ] **Max Results**: `20`
  - [ ] **Use LAN**: ✅ Checked
  - [ ] From **Results** array pin: Add **ForEachLoop**
  - [ ] From loop body: Add **Print String** for debugging (print session names)

### Function: JoinSession

- [ ] Click **+ Function**
- [ ] Name: `JoinSession`
- [ ] Add **Input** parameter:
  - [ ] Name: `SessionResult`
  - [ ] Type: **Blueprint Session Result**
- [ ] Add **Join Session** node
  - [ ] Connect **Session Result** parameter to it

**Save:**
- [ ] **Compile** → **Save** → Close

---

## ✅ Phase 6: Create Main Menu Widget

### WBP_MainMenu

**Creation:**
- [ ] Content Browser → Right-click
- [ ] **User Interface** → **Widget Blueprint**
- [ ] Name: `WBP_MainMenu`

**Design UI:**
- [ ] Open Widget Blueprint
- [ ] Switch to **Designer** tab

**Add Canvas Panel** (if not present):
- [ ] **Palette** panel (left) → Search: "Canvas"
- [ ] Drag **Canvas Panel** to hierarchy

**Add Vertical Box:**
- [ ] Palette → Search: "Vertical Box"
- [ ] Drag to Canvas Panel
- [ ] In **Details** (right):
  - [ ] Click **Anchors** → Select **Center** anchor
  - [ ] **Position X**: `0`, **Position Y**: `0`
  - [ ] **Size X**: `400`, **Size Y**: `600`
  - [ ] **Alignment**: X: `0.5`, Y: `0.5`

**Add Title Text:**
- [ ] Palette → "Text Block"
- [ ] Drag into **Vertical Box**
- [ ] In **Details**:
  - [ ] **Text**: "Multi Player Test"
  - [ ] **Font Size**: `48`
  - [ ] **Justification**: Center

**Add Spacer:**
- [ ] Palette → "Spacer"
- [ ] Drag into **Vertical Box** (below text)
- [ ] **Size**: `50`

**Add Host Button:**
- [ ] Palette → "Button"
- [ ] Drag into **Vertical Box**
- [ ] Rename in hierarchy: `Btn_Host`
- [ ] In **Details**:
  - [ ] Expand **Style** → **Normal**
  - [ ] Set desired button color/appearance
- [ ] Drag **Text Block** INTO the button (as child)
  - [ ] Text: "Host Game"
  - [ ] Font Size: `24`
  - [ ] Justification: Center

**Add Join Button:**
- [ ] Palette → "Button"
- [ ] Drag into **Vertical Box** (below Host button)
- [ ] Rename: `Btn_Join`
- [ ] Add **Text Block** child: "Join Game"

**Add Quit Button:**
- [ ] Palette → "Button"
- [ ] Drag into **Vertical Box** (below Join button)
- [ ] Rename: `Btn_Quit`
- [ ] Add **Text Block** child: "Quit Game"

**Add Button Functionality:**
- [ ] Switch to **Graph** tab
- [ ] In **Details** panel for **Btn_Host**, scroll to **Events** section
- [ ] Click **+** next to **On Clicked**

**In Event Graph for Btn_Host:**
- [ ] From **OnClicked (Btn_Host)** execution:
  - [ ] Add **Get Game Instance** node
  - [ ] From return value: **Cast To BP_MultiplayerGameInstance**
  - [ ] From **As BP Multiplayer Game Instance** pin:
    - [ ] Call **CreateSession** function (we created this earlier)
  - [ ] Add **Remove from Parent** node (removes menu from screen)

**Add Btn_Join functionality:**
- [ ] Select **Btn_Join** in Designer
- [ ] **Events** → **+ On Clicked**
- [ ] Similar to Host, but call **FindSessions** function
- [ ] Then call **JoinSession** (for now, just print debug info)

**Add Btn_Quit functionality:**
- [ ] Select **Btn_Quit** in Designer
- [ ] **Events** → **+ On Clicked**
- [ ] Add **Quit Game** node

**Save:**
- [ ] **Compile** → **Save** → Close

---

## ✅ Phase 7: Create Game Levels

### MAP_Multiplayer (Main Game Level)

**Creation:**
- [ ] **File** → **New Level**
- [ ] Select **Empty Level** or **Default**
- [ ] **File** → **Save Current Level As...**
- [ ] Name: `MAP_Multiplayer`
- [ ] Save in `Content/Maps/` (create folder if needed)

**Add Basic Geometry:**
- [ ] **Place Actors** panel (or press Shift+1)
- [ ] **Basic** → Drag **Plane** or **Cube** into viewport
- [ ] Select floor, press **F** to focus
- [ ] In **Details**:
  - [ ] **Scale**: X: `100`, Y: `100`, Z: `1`
  - [ ] **Location**: X: `0`, Y: `0`, Z: `0`

**Add Lighting:**
- [ ] **Place Actors** → **Lights**
- [ ] Drag **Directional Light** into level
  - [ ] Position above floor (Z: `500`)
  - [ ] Rotation: Pitch: `-45` (pointing downward)
- [ ] **Visual Effects** → Drag **Sky Atmosphere**
- [ ] **Lights** → Drag **Sky Light**
  - [ ] In Details: **Source Type**: SLS Captured Scene

**Add Player Start Points (CRITICAL):**
- [ ] **Place Actors** → **All Classes** → Search: "Player Start"
- [ ] Drag **Player Start** into level
  - [ ] Position: X: `0`, Y: `0`, Z: `100`
- [ ] Duplicate (Ctrl+D or Alt+Drag) to create 3 more
  - [ ] PlayerStart 2: X: `500`, Y: `0`, Z: `100`
  - [ ] PlayerStart 3: X: `0`, Y: `500`, Z: `100`
  - [ ] PlayerStart 4: X: `500`, Y: `500`, Z: `100`

**Add Navigation (Optional):**
- [ ] **Place Actors** → **Volumes** → **Nav Mesh Bounds Volume**
- [ ] Scale to cover playable area
- [ ] Press **P** key to toggle nav mesh visualization

**Build Lighting:**
- [ ] **Build** → **Build Lighting Only** (or F7)
- [ ] Wait for build to complete

**Save:**
- [ ] **File** → **Save Current Level**
- [ ] **File** → **Save All**

---

### MAP_MainMenu (Menu Level)

**Creation:**
- [ ] **File** → **New Level**
- [ ] **Empty Level**
- [ ] **File** → **Save Current Level As...**
- [ ] Name: `MAP_MainMenu`

**Add Simple Background (Optional):**
- [ ] Add basic lighting (Directional Light, Sky Atmosphere)
- [ ] Keep it simple - this is just for UI

**Add Widget Display Logic:**
- [ ] **Blueprints** → **Open Level Blueprint**
- [ ] In Event Graph:

**From Event BeginPlay:**
- [ ] Add **Create Widget** node
  - [ ] **Class**: `WBP_MainMenu`
- [ ] From **Return Value**:
  - [ ] Add **Add to Viewport** node
- [ ] Then add **Get Player Controller** (player index 0)
- [ ] From controller:
  - [ ] Add **Set Show Mouse Cursor** (set to True)
  - [ ] Add **Set Input Mode UI Only** node

**Save:**
- [ ] **Compile** → **Save**
- [ ] Close Level Blueprint
- [ ] **File** → **Save All**

---

## ✅ Phase 8: Configure Project Settings

### Set Default Classes

- [ ] **Edit** → **Project Settings**
- [ ] **Project** → **Maps & Modes**

**Default Modes:**
- [ ] **Default GameMode**: `BP_MultiplayerGameMode`

**Selected GameMode (auto-populates when you select Default GameMode):**
- [ ] **Default Pawn Class**: `BP_PlayerCharacter`
- [ ] **HUD Class**: None
- [ ] **Player Controller Class**: `BP_MultiplayerController`
- [ ] **Game State Class**: GameStateBase
- [ ] **Player State Class**: PlayerState

**Default Maps:**
- [ ] **Editor Startup Map**: `MAP_Multiplayer`
- [ ] **Game Default Map**: `MAP_MainMenu`
- [ ] **Server Default Map**: `MAP_Multiplayer`

### Set Game Instance

- [ ] Still in **Project Settings**
- [ ] **Project** → **Maps & Modes**
- [ ] Scroll down to find **Game Instance Class**
- [ ] **Game Instance Class**: `BP_MultiplayerGameInstance`

### Configure Input Mappings

- [ ] **Engine** → **Input**

**Axis Mappings:**
- [ ] Click **+** next to **Axis Mappings**
- [ ] Name: `MoveForward`
  - [ ] Add: **W** key, Scale: `1.0`
  - [ ] Add: **S** key, Scale: `-1.0`
  - [ ] Add: **Gamepad Left Thumbstick Y-Axis**, Scale: `1.0`

- [ ] **+** Axis Mapping
- [ ] Name: `MoveRight`
  - [ ] Add: **D** key, Scale: `1.0`
  - [ ] Add: **A** key, Scale: `-1.0`
  - [ ] Add: **Gamepad Left Thumbstick X-Axis**, Scale: `1.0`

- [ ] **+** Axis Mapping
- [ ] Name: `Turn`
  - [ ] Add: **Mouse X**, Scale: `1.0`
  - [ ] Add: **Gamepad Right Thumbstick X-Axis**, Scale: `1.0`

- [ ] **+** Axis Mapping
- [ ] Name: `LookUp`
  - [ ] Add: **Mouse Y**, Scale: `-1.0`
  - [ ] Add: **Gamepad Right Thumbstick Y-Axis**, Scale: `1.0`

**Action Mappings:**
- [ ] Click **+** next to **Action Mappings**
- [ ] Name: `Jump`
  - [ ] Add: **Space Bar**
  - [ ] Add: **Gamepad Face Button Bottom** (A/X button)

- [ ] **Close** Project Settings

---

## ✅ Phase 9: Testing

### Test Split-Screen Local Co-op

- [ ] Make sure `MAP_Multiplayer` is the active level
- [ ] Click **▼** arrow next to **Play** button
- [ ] Select **Advanced Settings...**

**Configure PIE (Play In Editor) Settings:**
- [ ] **Number of Players**: `2`
- [ ] **Net Mode**: **Play As Listen Server**
- [ ] **Run Under One Process**: ✅ Checked
- [ ] **Use Single Process**: ✅ Checked
- [ ] **Editor Multiplayer Mode** section:
  - [ ] Window Size: `800x600` (or as desired)
  
- [ ] Click **Play** (or Alt+P)

**Expected Results:**
- [ ] 2 viewports appear (split screen)
- [ ] Each shows a mannequin character
- [ ] Each player can move independently with WASD
- [ ] Cameras follow their respective characters

**Troubleshooting:**
- ❌ Only 1 player? → Check Game Instance has Create Player node
- ❌ No split? → Verify PIE settings Number of Players = 2
- ❌ Can't move? → Check Input Mappings and Character input events
- ❌ Black screen? → Check level has lighting
- ❌ Characters floating? → Check Player Start Z positions (should be on floor)

### Test Online Multiplayer

**Method 1: Two Editor Instances**
- [ ] Close current PIE session
- [ ] **Play** → **Advanced Settings**
- [ ] Set **Number of Players**: `1`
- [ ] Set **Run Dedicated Server**: ✅ Checked
- [ ] Or use **Net Mode**: **Play As Client**
- [ ] Click Play in first instance (Host)
- [ ] Open second UE Editor instance of same project
- [ ] In second instance: Press **~** (tilde) to open console
- [ ] Type: `open 127.0.0.1`
- [ ] Press Enter

**Method 2: Standalone**
- [ ] **Play** → **Standalone Game**
- [ ] In first window: Click "Host Game" in main menu
- [ ] Launch second instance
- [ ] In second window: Click "Join Game"

**Expected Results:**
- [ ] Characters from both instances visible to each other
- [ ] Movement replicates smoothly
- [ ] Both players can interact with environment

**Troubleshooting:**
- ❌ Can't connect? → Check Online Subsystem config in DefaultEngine.ini
- ❌ Character doesn't appear? → Check Replicates = true in BP_PlayerCharacter
- ❌ Movement jerky? → Check Replicate Movement = true

---

## 🎉 Completion Checklist

- [ ] Mannequin assets in project
- [ ] BP_MultiplayerGameMode created and configured
- [ ] BP_PlayerCharacter with mannequin, camera, input, replication
- [ ] BP_MultiplayerController created
- [ ] BP_MultiplayerGameInstance with session functions
- [ ] WBP_MainMenu widget created with Host/Join buttons
- [ ] MAP_Multiplayer level with floor, lights, 4 Player Starts
- [ ] MAP_MainMenu level with UI display
- [ ] Project Settings configured (classes, maps, input)
- [ ] Split-screen tested successfully (2 local players)
- [ ] Online multiplayer tested successfully (2 instances)

**Your multiplayer foundation is complete! 🚀**

---

## Next Steps

After completing this checklist:
- Add game mechanics (objectives, scoring)
- Create additional UI (session browser, player names)
- Add sound effects and visual polish
- Implement voice/text chat
- Test on LAN with multiple machines
- Deploy to Epic Online Services

**Questions? Refer to MULTIPLAYER_IMPLEMENTATION_GUIDE.md for detailed explanations!**

