# Asset Paths Reference - Third Person Content

Based on the git commit showing 248 files added, here are the exact asset paths in your project:

---

## 🎭 **Character Meshes**

### Male Mannequin (Manny)
```
/Game/Characters/Mannequins/Meshes/SKM_Manny_Simple
```
- **Lightweight version** - Recommended for multiplayer
- Simple mesh with essential bones

### Female Mannequin (Quinn)  
```
/Game/Characters/Mannequins/Meshes/SKM_Quinn_Simple
```
- **Lightweight version**
- Simple mesh with essential bones

### Full Skeleton
```
/Game/Characters/Mannequins/Meshes/SK_Mannequin
```
- Full rigged skeleton used by both Manny and Quinn

---

## 🎬 **Animation Blueprints**

### Unarmed Animations (Recommended)
```
/Game/Characters/Mannequins/Anims/Unarmed/ABP_Unarmed
```
- Basic locomotion (walk, run, jump, idle)
- No weapons
- Perfect for multiplayer co-op testing

### Class Reference Format (for MCP)
```
/Game/Characters/Mannequins/Anims/Unarmed/ABP_Unarmed.ABP_Unarmed_C
```

---

## 🎨 **Materials**

### Mannequin Material
```
/Game/Characters/Mannequins/Materials/M_Mannequin
```

### Manny Material Instances
```
/Game/Characters/Mannequins/Materials/Manny/MI_Manny_01_New
/Game/Characters/Mannequins/Materials/Manny/MI_Manny_02_New
```

### Quinn Material Instances
```
/Game/Characters/Mannequins/Materials/Quinn/MI_Quinn_01
/Game/Characters/Mannequins/Materials/Quinn/MI_Quinn_02
```

---

## 🏃 **Individual Animations**

### Unarmed Movement
```
/Game/Characters/Mannequins/Anims/Unarmed/MM_Idle
/Game/Characters/Mannequins/Anims/Unarmed/Jog/MF_Unarmed_Jog_Fwd
/Game/Characters/Mannequins/Anims/Unarmed/Walk/MF_Unarmed_Walk_Fwd
/Game/Characters/Mannequins/Anims/Unarmed/Jump/MM_Jump
/Game/Characters/Mannequins/Anims/Unarmed/Jump/MM_Fall_Loop
/Game/Characters/Mannequins/Anims/Unarmed/Jump/MM_Land
```

### Blend Spaces
```
/Game/Characters/Mannequins/Anims/Unarmed/BS_Idle_Walk_Run
```

---

## 🎮 **Example Content**

### Third Person Example Character
```
/Game/ThirdPerson/Blueprints/BP_ThirdPersonCharacter
/Game/ThirdPerson/Blueprints/BP_ThirdPersonGameMode
/Game/ThirdPerson/Blueprints/BP_ThirdPersonPlayerController
```

### Example Level
```
/Game/ThirdPerson/Lvl_ThirdPerson
```

---

## 🔧 **How to Use These Paths**

### In Blueprint Editor (Manual)
1. Open the asset picker dropdown
2. Type part of the name (e.g., "Manny", "ABP", "Unarmed")
3. Select from filtered results

### In MCP Commands (Automated)
```python
# Set skeletal mesh
set_component_property(
    blueprint_name="BP_PlayerCharacter",
    component_name="Mesh",
    property_name="SkeletalMesh",
    property_value="/Game/Characters/Mannequins/Meshes/SKM_Manny_Simple"
)

# Set animation blueprint (use _C suffix for class reference)
set_component_property(
    blueprint_name="BP_PlayerCharacter",
    component_name="Mesh",
    property_name="AnimClass",
    property_value="/Game/Characters/Mannequins/Anims/Unarmed/ABP_Unarmed.ABP_Unarmed_C"
)
```

### In C++ Code
```cpp
// Get the skeletal mesh
static ConstructorHelpers::FObjectFinder<USkeletalMesh> MannequinMesh(
    TEXT("/Game/Characters/Mannequins/Meshes/SKM_Manny_Simple")
);

// Get the animation blueprint class
static ConstructorHelpers::FClassFinder<UAnimInstance> AnimBP(
    TEXT("/Game/Characters/Mannequins/Anims/Unarmed/ABP_Unarmed")
);
```

---

## 📁 **Content Browser Locations**

To browse visually in Unreal Editor:

1. **Characters**: `Content → Characters → Mannequins`
   - `Meshes/` - Character models
   - `Anims/` - All animations
   - `Materials/` - Character materials
   - `Textures/` - Texture files

2. **Example Content**: `Content → ThirdPerson`
   - `Blueprints/` - Working example characters
   - `Lvl_ThirdPerson.umap` - Test level

3. **Level Prototyping**: `Content → LevelPrototyping`
   - `Meshes/` - Basic shapes (cubes, ramps, cylinders)
   - `Materials/` - Grid materials
   - `Interactable/` - Jump pads, doors, targets

4. **Input**: `Content → Input`
   - `Actions/` - Input action assets (IA_Move, IA_Jump, etc.)
   - `IMC_Default` - Input mapping context

---

## ✅ **Quick Copy-Paste Asset Paths**

For the fastest manual setup, use these:

**Skeletal Mesh:**
```
SKM_Manny_Simple
```

**Animation Blueprint:**
```
ABP_Unarmed
```

**Example Reference Character:**
```
BP_ThirdPersonCharacter
```

Just paste these names into the search boxes in Unreal Editor!

---

*All paths confirmed from git commit showing 248 files added*
*Last updated: 2025-10-26*

