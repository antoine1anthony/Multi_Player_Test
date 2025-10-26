# Quick Fix: Add Mannequin to BP_PlayerCharacter

## 🎯 **5-Minute Manual Setup**

Since the MCP auto-configuration needs verification, follow these simple steps:

---

## Step 1: Open BP_PlayerCharacter (30 seconds)

1. In Unreal Editor, open **Content Browser** (bottom panel)
2. Navigate to **Content → Blueprints**
3. **Double-click** `BP_PlayerCharacter`

---

## Step 2: Select the Mesh Component (10 seconds)

1. Look at the **Components** panel (top-left of the Blueprint Editor)
2. Click on **Mesh (Inherited)** - it's under the character hierarchy
   - Should show a capsule with a small mesh icon

---

## Step 3: Assign the Skeletal Mesh (1 minute)

1. Look at the **Details** panel (right side)
2. Find the **Mesh** section at the top
3. Click the dropdown next to **Skeletal Mesh**
4. Type `"Manny"` in the search box
5. Select one of these (any will work):
   - **SKM_Manny_Simple** (recommended - lighter)
   - **SKM_Quinn_Simple** (female character)
   - **SK_Mannequin** (full version)

✅ **You should immediately see a blue/gray character appear in the viewport!**

---

## Step 4: Fix the Position/Rotation (30 seconds)

Still in the **Details** panel, scroll down to **Transform**:

1. **Location**:
   - X: `0`
   - Y: `0`
   - Z: `-90` (moves character down into the capsule)

2. **Rotation**:
   - Pitch: `0`
   - Yaw: `-90` (rotates character to face forward)
   - Roll: `0`

✅ **Character should now be standing upright and centered!**

---

## Step 5: Add Animation Blueprint (1 minute)

Still in **Details** panel:

1. Scroll down to **Animation** section
2. Click the dropdown next to **Anim Class**
3. Type `"ABP"` in the search box
4. Select **ABP_Unarmed** (or ABP_Manny if available)

✅ **Character will now animate when moving!**

---

## Step 6: Compile and Save (10 seconds)

1. Click the **Compile** button (top toolbar - green checkmark)
2. Click the **Save** button (top toolbar - floppy disk icon)
3. Close the Blueprint Editor

---

## 🎮 **Test It!**

1. Click **Play** (green play button at top) or press **Alt+P**
2. Use **WASD** to move
3. Press **Spacebar** to jump

You should now see a visible, animated character! 🎉

---

## 🚨 **Still Can't Find Mannequin Assets?**

If the dropdowns are empty or you can't find "Manny":

### Option A: Verify Content Pack Installed
1. **Content Browser** → Look for `Content/Characters/Mannequins/` folder
2. If missing, the content pack didn't install properly

### Option B: Re-add Content Pack
1. **Content Browser** → Click **Add** button (green plus)
2. Select **Add Feature or Content Pack**
3. Find **Third Person** or **Character Content**
4. Click **Add to Project**

### Option C: Check Example Character
1. Navigate to **Content → ThirdPerson → Blueprints**
2. Open **BP_ThirdPersonCharacter** (this is the example)
3. Select **Mesh** component
4. Look at what Skeletal Mesh it uses
5. Copy that asset reference to your BP_PlayerCharacter

---

## 📸 **What Success Looks Like**

**In Blueprint Editor Viewport:**
- Blue/gray humanoid character visible
- Character standing upright in the capsule
- Camera boom (spring arm) visible above character

**In-Game (when you hit Play):**
- You spawn as a visible character (not invisible)
- Character animates when walking
- Camera follows behind character

---

## ⚡ **Quick Troubleshooting**

| Problem | Solution |
|---------|----------|
| Character is lying down | Set Rotation Yaw to -90 |
| Character is floating | Set Location Z to -90 |
| No animation | Set Anim Class to ABP_Unarmed |
| Can't find assets | Re-add Third Person content pack |
| Character is invisible in-game | Check that Mesh is set under Components |

---

*This should take less than 5 minutes total!*
*If you get stuck, send a screenshot of your Blueprint Editor and I'll help diagnose.*

