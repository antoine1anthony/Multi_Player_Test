# Multiplayer Implementation Guide for Multi_Player_Test

This guide provides step-by-step instructions for implementing the multiplayer system with 2 mannequins, supporting both online and split-screen local co-op.

## Prerequisites Completed

✅ **Plugins Enabled**: OnlineSubsystem, OnlineSubsystemNull, OnlineSubsystemUtils
✅ **Network Configuration**: Online Subsystem configured in DefaultEngine.ini
✅ **Project**: C++ support added

---

## Phase 1: Add Third Person Character Assets

### Step 1.1: Get Mannequin Assets from Epic Marketplace

**Option A: From Epic Games Launcher (Recommended)**

1. Open **Epic Games Launcher**
2. Go to **Unreal Engine** → **Library** tab
3. Scroll down to **Vault** section
4. Search for **"Third Person"** or **"Mannequin"**
5. Find the **"Third Person Character"** content pack (free)
6. Click **Add to Project**
7. Select your **Multi_Player_Test** project
8. Click **Add to Project** to confirm

**Option B: Create Temporary Project and Migrate**

1. In Unreal Engine Launcher, click **Launch** UE 5.6
2. Create a **New Project** → Select **Third Person** template
3. Name it `TempThirdPerson` → **Create**
4. Once loaded, in Content Browser, navigate to `Content/ThirdPerson/`
5. Right-click the `Characters` folder → **Asset Actions** → **Migrate**
6. Select your `Multi_Player_Test` project's Content folder
7. Click **OK** to migrate assets
8. Close the temp project (can delete it after)

### What You Should Have:

- `Content/Characters/Mannequins/` folder with skeletal meshes
- `SK_Mannequin` skeletal mesh
- Mannequin animations and Animation Blueprint

---

## Phase 2: Create Core Multiplayer Blueprint Classes

### Step 2.1: Create Game Mode Blueprint

1. In **Content Browser**, right-click → **Blueprint Class**
2. Select **Game Mode Base**
3. Name it `BP_MultiplayerGameMode`
4. **Double-click** to open it
5. In **Class Defaults** panel (right side), set:
   - **Number of Players**: `4` (allows up to 4 for testing)
   - Save and close

### Step 2.2: Create Player Character Blueprint

1. **Content Browser** → Right-click → **Blueprint Class**
2. Select **Character** class
3. Name it `BP_PlayerCharacter`
4. **Double-click** to open the Blueprint Editor

#### Configure Character Components:

**In the Components Panel (left):**

5. Select **Mesh** (CharacterMesh0) component
6. In **Details** panel:

   - **Skeletal Mesh**: Select `SK_Mannequin` (or your imported mannequin)
   - **Location**: `X=0, Y=0, Z=-90`
   - **Rotation**: `X=0, Y=0, Z=-90`
   - **Animation Mode**: Use Animation Blueprint
   - **Anim Class**: Select the mannequin's Animation Blueprint (ABP_Mannequin or similar)

7. Select **CharacterMovement** component
8. In **Details** panel:

   - **Max Walk Speed**: `600.0`
   - **Replication** section:
     - Check **Replicate Movement**

9. Click **Add Component** button → **Camera**
10. Drag **Camera** onto **SpringArm** (create SpringArm first if needed)

11. **Add Component** → **Spring Arm**
12. Configure Spring Arm:

    - **Target Arm Length**: `400.0`
    - **Location**: `X=0, Y=0, Z=90` (shoulder height)
    - **Use Pawn Control Rotation**: ✅ Checked
    - **Inherit Pitch/Yaw/Roll**: ✅ All Checked

13. Drag **Camera** onto **Spring Arm** (make it a child)

#### Configure Replication:

14. Click **Class Defaults** button (top toolbar)
15. In **Details** panel:
    - **Replication** section:
      - **Replicates**: ✅ Checked
      - **Replicate Movement**: ✅ Checked (should already be set)
    - **Pawn** section:
      - **Auto Possess Player**: **Disabled** (important for multiplayer!)
      - **Auto Possess AI**: **Disabled**

#### Add Input Mapping:

16. Go to **Event Graph** tab
17. We'll add input later, but for now, let's set up basic movement

**Add Movement Input:**

18. Right-click in Event Graph → Search for **Input Action Move** (if using Enhanced Input)
    - OR use **InputAxis MoveForward** and **InputAxis MoveRight** (traditional)
19. Connect to **Add Movement Input** nodes
20. Set **World Direction** for each axis appropriately

**Quick Traditional Input Setup:**

21. Right-click → **InputAxis MoveForward**
22. Drag from execution → **Add Movement Input**
23. Right-click **Add Movement Input** node, get **Get Control Rotation**
24. From Get Control Rotation, use **Get Forward Vector**
25. Connect to **World Direction** pin
26. Connect **Axis Value** to **Scale Value** pin

27. Repeat for **InputAxis MoveRight** with **Get Right Vector**

**Add Look Input:**

28. Right-click → **InputAxis Turn**
29. Connect to **Add Controller Yaw Input**

30. Right-click → **InputAxis LookUp**
31. Connect to **Add Controller Pitch Input**

32. **Compile**, **Save**, and **Close**

### Step 2.3: Create Player Controller Blueprint

1. **Content Browser** → Right-click → **Blueprint Class**
2. Select **Player Controller**
3. Name it `BP_MultiplayerController`
4. Open it
5. In **Class Defaults**:
   - **Show Mouse Cursor**: `false` (for third-person gameplay)
6. **Compile**, **Save**, **Close**

### Step 2.4: Create Game Instance Blueprint

1. **Content Browser** → Right-click → **Blueprint Class**
2. Select **Game Instance**
3. Name it `BP_MultiplayerGameInstance`
4. Open the Blueprint
5. We'll add split-screen and session logic here in the next phases
6. **Save** and **Close** for now

---

## Phase 3: Implement Split-Screen Local Co-op

### Step 3.1: Configure Game Instance for Split-Screen

1. Open `BP_MultiplayerGameInstance`
2. Go to **Event Graph**

#### Add Local Player 2:

3. Find **Event Init** node (or create it)
4. From Event Init execution:
   - Add **Create Player** node
   - **Player Index**: `1` (this creates Player 2)
   - **Spawn Pawn If Necessary**: ✅ Checked
5. **Compile** and **Save**

### Step 3.2: Configure Project Settings for Local Multiplayer

1. Go to **Edit** → **Project Settings**
2. Navigate to **Engine** → **General Settings**
3. Under **Default Classes**:
   - **Game Instance Class**: Select `BP_MultiplayerGameInstance`
4. Close Project Settings

---

## Phase 4: Implement Online Multiplayer

### Step 4.1: Enable Network Replication (Already Done)

We already configured replication in `BP_PlayerCharacter` in Step 2.2.

### Step 4.2: Create UI Widgets for Session Management

#### Create Main Menu Widget:

1. **Content Browser** → Right-click → **User Interface** → **Widget Blueprint**
2. Name it `WBP_MainMenu`
3. Open it

**Design the Main Menu:**

4. Drag a **Canvas Panel** to cover the screen (if not already there)
5. Add a **Vertical Box** centered on screen
6. Inside Vertical Box, add:
   - **Text Block**: "Multi Player Test - Main Menu"
   - **Button**: Name it `Btn_Host`
     - Add **Text** child: "Host Game"
   - **Button**: Name it `Btn_Join`
     - Add **Text** child: "Join Game"
   - **Button**: Name it `Btn_Quit`
     - Add **Text** child: "Quit"

**Add Button Functionality:**

7. Go to **Graph** tab
8. In **Designer** tab, select `Btn_Host`
9. In **Details**, scroll to **Events** → Click **+** next to **On Clicked**
10. In Event Graph, from **OnClicked (Btn_Host)**:

    - Add **Get Game Instance** node
    - Cast to `BP_MultiplayerGameInstance`
    - Call a custom function **CreateSession** (we'll create this next)

11. Repeat for `Btn_Join` → call **FindSessions** function
12. For `Btn_Quit` → **Quit Game** node

13. **Compile** and **Save**

#### Create Session Functions in Game Instance:

14. Open `BP_MultiplayerGameInstance`
15. Add a new **Function** called `CreateSession`

**CreateSession Function:**

16. In the function graph:

    - Add **Create Session** node
    - **Public Connections**: `1` (LAN connections)
    - **Number of Public Connections**: `4`
    - **Use LAN**: ✅ Checked (for local network testing)
    - **Session Name**: `GameSession`

17. From **Create Session** Success pin:

    - Add **Open Level** node
    - **Level Name**: `MAP_Multiplayer` (we'll create this)
    - **Options**: `?listen` (makes this a listen server)

18. Add a new **Function** called `FindSessions`

**FindSessions Function:**

19. In the function graph:

    - Add **Find Sessions** node
    - **Max Results**: `20`
    - **Use LAN**: ✅ Checked

20. From **Results** pin:

    - Add **ForEachLoop**
    - Print session names (for debugging)
    - Later, we'll populate a UI list

21. Add a new **Function** called `JoinSession`
    - Parameter: **Session Result** (type: BlueprintSessionResult)

**JoinSession Function:**

22. In the function graph:

    - Add **Join Session** node
    - Connect **Session Result** parameter to it

23. **Compile**, **Save**, **Close**

---

## Phase 5: Create Game Levels

### Step 5.1: Create Main Game Map

1. **File** → **New Level**
2. Select **Empty Level**
3. **File** → **Save Current Level As...**
4. Name it `MAP_Multiplayer`

**Add Basic Geometry:**

5. In **Place Actors** panel (or **Modes** panel), search for **Plane**
6. Drag a **Plane** into the level (or create a **Cube** scaled as floor)
7. Scale it to create a large floor: **Scale (100, 100, 1)**
8. Position at `X=0, Y=0, Z=0`

**Add Lighting:**

9. **Place Actors** → **Lights** → Drag **Directional Light** into level
10. Position above the floor
11. Rotate to cast light downward

12. **Place Actors** → **Visual Effects** → Drag **Sky Atmosphere** into level
13. Add **Sky Light** for ambient lighting

**Add Player Start Points:**

14. **Place Actors** → **Basic** → Drag **Player Start** into level
15. Position it on the floor: `X=0, Y=0, Z=100`
16. Duplicate it (**Alt + Drag** or **Ctrl+D**)
17. Move the second **Player Start** away: `X=500, Y=0, Z=100`
18. Add 2 more Player Starts at different locations for a total of 4

**Add Navigation (Optional but Recommended):**

19. **Place Actors** → **Volumes** → Drag **Nav Mesh Bounds Volume** into level
20. Scale it to cover your playable area

**Build Lighting:**

21. **Build** → **Build Lighting Only** (or **Build All**)
22. **File** → **Save All**

### Step 5.2: Create Main Menu Map

1. **File** → **New Level**
2. Select **Empty Level** (or Default for simple background)
3. **File** → **Save Current Level As...**
4. Name it `MAP_MainMenu`

**Add Main Menu Widget Display:**

5. Open **Level Blueprint** (**Blueprints** → **Open Level Blueprint**)
6. From **Event BeginPlay**:

   - Add **Create Widget** node
   - **Class**: Select `WBP_MainMenu`
   - From **Return Value**, add **Add to Viewport**
   - Add **Set Show Mouse Cursor** (Get Player Controller → Set Show Mouse Cursor = True)
   - Add **Set Input Mode UI Only** node (Get Player Controller → Set Input Mode UI Only)

7. **Compile**, **Save**, and close Level Blueprint
8. **File** → **Save All**

---

## Phase 6: Configure Project Settings

### Step 6.1: Set Default Classes

1. **Edit** → **Project Settings**
2. Navigate to **Project** → **Maps & Modes**

**Set Default Game Mode:**

3. **Default GameMode**: Select `BP_MultiplayerGameMode`
4. Under **Selected GameMode** section:
   - **Default Pawn Class**: `BP_PlayerCharacter`
   - **Player Controller Class**: `BP_MultiplayerController`
   - **HUD Class**: None (for now)
   - **Game State Class**: GameStateBase (default)
   - **Player State Class**: PlayerState (default)

### Step 6.2: Set Default Maps

5. Still in **Project Settings** → **Maps & Modes**
6. **Default Maps** section:

   - **Editor Startup Map**: `MAP_Multiplayer`
   - **Game Default Map**: `MAP_MainMenu`
   - **Transition Map**: None
   - **Server Default Map**: `MAP_Multiplayer`

7. **Close** Project Settings

### Step 6.3: Setup Input Mappings

1. **Edit** → **Project Settings**
2. Navigate to **Engine** → **Input**

**Add Axis Mappings:**

3. Expand **Axis Mappings** → Click **+** to add:

   - **MoveForward**:
     - **W** key: Scale `1.0`
     - **S** key: Scale `-1.0`
     - **Gamepad Left Thumbstick Y-Axis**: Scale `1.0`
   - **MoveRight**:
     - **D** key: Scale `1.0`
     - **A** key: Scale `-1.0`
     - **Gamepad Left Thumbstick X-Axis**: Scale `1.0`
   - **Turn**:
     - **Mouse X**: Scale `1.0`
     - **Gamepad Right Thumbstick X-Axis**: Scale `1.0`
   - **LookUp**:
     - **Mouse Y**: Scale `-1.0`
     - **Gamepad Right Thumbstick Y-Axis**: Scale `1.0`

4. **Add Action Mappings** (for jump, etc.):

   - **Jump**:
     - **Space Bar**
     - **Gamepad Face Button Bottom** (A/X)

5. **Close** Project Settings

### Step 6.4: Update Character Input (If Needed)

1. Open `BP_PlayerCharacter`
2. In **Event Graph**, verify your input events match the axis mappings above
3. If using **Enhanced Input System** (UE5 default), you may need to create Input Actions separately

---

## Phase 7: Testing

### Step 7.1: Test Split-Screen Locally

1. Make sure you're on `MAP_Multiplayer` level
2. Click **Play** dropdown arrow (next to Play button)
3. Select **Advanced Settings...**

**Configure PIE Settings:**

4. In **Play In Editor** settings:

   - **Number of Players**: `2`
   - **Net Mode**: **Play As Listen Server**
   - **Run Under One Process**: ✅ Checked
   - **Use Single Process**: ✅ Checked

5. Click **Play** (or press **Alt+P**)

**Expected Result:**

- You should see 2 viewports (split screen)
- Each viewport shows a different mannequin character
- Both characters can move independently
- Both cameras follow their respective characters

**Troubleshooting:**

- If only 1 player spawns: Check `BP_MultiplayerGameInstance` has **Create Player** node
- If no split: Verify **Number of Players** = 2 in PIE settings
- If characters don't move: Check Input Mappings and Character Blueprint input setup

### Step 7.2: Test Online Multiplayer (Network)

**Option A: Two Editor Instances (Recommended)**

1. **Play** dropdown → **Advanced Settings**
2. Set:

   - **Number of Players**: `1`
   - **Net Mode**: **Play As Listen Server**
   - **Editor Multiplayer Mode**: Check **Run Dedicated Server**
   - OR use **Play As Client** in one instance

3. Launch **2 instances** of the editor:
   - Instance 1: Click **Play** (Host)
   - Instance 2: Open console (~ key) → Type: `open 127.0.0.1` → Press Enter

**Option B: Standalone Mode**

1. **Play** dropdown → **Standalone Game** (or **Alt+Shift+P**)
2. Launch 2 windows:
   - Window 1: Host via Main Menu
   - Window 2: Join via Main Menu (use IP `127.0.0.1`)

**Expected Result:**

- Player from one instance appears in the other instance's game
- Characters move and replicate between instances
- Both players can see each other

**Troubleshooting:**

- If connection fails: Check **Online Subsystem** is configured (already done in config)
- If player doesn't spawn: Verify **Player Start** actors in level
- If character doesn't replicate: Check **Replicates** = true in `BP_PlayerCharacter`

---

## Phase 8: Enhancements (Optional)

### Add Player Name Tags

1. Create a **Widget Blueprint**: `WBP_PlayerNameTag`
2. Add a **Text Block** showing "Player X"
3. In `BP_PlayerCharacter`:
   - Add **Widget Component**
   - Set **Widget Class**: `WBP_PlayerNameTag`
   - Set **Space**: World

### Add Different Player Colors

1. In `BP_PlayerCharacter` **Event BeginPlay**:
2. Get **Player Controller**
3. Get **Player Index** (or unique ID)
4. Based on index, set different material color on the mannequin mesh

### Improve Session Browser

1. Create `WBP_SessionList` widget
2. Populate it with found sessions from `FindSessions`
3. Add buttons to join specific sessions

---

## Summary Checklist

✅ Mannequin assets added to project
✅ `BP_MultiplayerGameMode` created and configured
✅ `BP_PlayerCharacter` created with mannequin, camera, movement, and replication
✅ `BP_MultiplayerController` created
✅ `BP_MultiplayerGameInstance` created with CreateSession/FindSessions/JoinSession
✅ Split-screen configured (Create Player for Player 2)
✅ UI widgets created: `WBP_MainMenu`
✅ `MAP_Multiplayer` level created with floor, lighting, and 4 Player Starts
✅ `MAP_MainMenu` level created with UI display
✅ Project Settings configured (Default classes, maps, input)
✅ Split-screen tested (2 local players, separate viewports)
✅ Online multiplayer tested (2 editor instances or standalone)

---

## Next Steps

- Add game mechanics (shooting, health, objectives)
- Create matchmaking UI with session list
- Add player name tags and identification
- Implement game state synchronization
- Add sound effects and polish
- Test on LAN with multiple machines
- Deploy to Epic Online Services for internet play

**Your multiplayer foundation is now complete!**
