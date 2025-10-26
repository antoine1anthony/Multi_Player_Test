# Multi_Player_Test

A multiplayer game project for Unreal Engine 5.6 with C++ and Blueprint support, featuring both online and local split-screen co-op gameplay with mannequin characters.

## Project Status

✅ C++ Support Added
✅ Git Repository Initialized
✅ Multiplayer Plugins Configured
✅ Online Subsystem Configured
✅ Implementation Guide Created

## Quick Start

### Prerequisites

- Unreal Engine 5.6
- Visual Studio 2022 (for C++ compilation)
- Epic Games Launcher (for mannequin assets)

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/antoine1anthony/Multi_Player_Test.git
   cd Multi_Player_Test
   ```

2. **Generate Project Files**

   - Right-click `Multi_Player_Test.uproject`
   - Select "Generate Visual Studio project files"

3. **Build the Project**

   - Open `Multi_Player_Test.sln` in Visual Studio
   - Set build configuration to **Development Editor** | **Win64**
   - Build the solution (F7)

4. **Follow the Implementation Guide**
   - Open `MULTIPLAYER_IMPLEMENTATION_GUIDE.md`
   - Follow the step-by-step instructions to create the multiplayer system

## Features

- **Online Multiplayer**: Host and join games over LAN or internet
- **Split-Screen Local Co-op**: 2 players on the same screen
- **Character System**: Third-person mannequin characters with animations
- **Network Replication**: Smooth character movement synchronization
- **Session Management**: Create, find, and join multiplayer sessions

## Project Structure

```
Multi_Player_Test/
├── Config/                     # Project configuration files
│   ├── DefaultEngine.ini      # Engine settings (Online Subsystem configured)
│   ├── DefaultGame.ini
│   └── DefaultInput.ini
├── Content/                    # Game assets (created in Unreal Editor)
│   ├── Blueprints/            # Blueprint classes (to be created)
│   ├── Characters/            # Mannequin assets (to be added)
│   ├── Maps/                  # Game levels (to be created)
│   └── UI/                    # Widget blueprints (to be created)
├── Source/                     # C++ source code
│   ├── Multi_Player_Test/     # Main game module
│   │   ├── Multi_Player_Test.h
│   │   ├── Multi_Player_Test.cpp
│   │   └── Multi_Player_Test.Build.cs
│   ├── Multi_Player_Test.Target.cs
│   └── Multi_Player_TestEditor.Target.cs
├── MULTIPLAYER_IMPLEMENTATION_GUIDE.md  # Detailed implementation guide
└── Multi_Player_Test.uproject  # Unreal project file
```

## Implementation Plan

The multiplayer system is implemented in phases:

1. **Phase 1**: Add Third Person Character Assets (Mannequins)
2. **Phase 2**: Create Core Multiplayer Blueprint Classes
   - BP_MultiplayerGameMode
   - BP_PlayerCharacter
   - BP_MultiplayerController
   - BP_MultiplayerGameInstance
3. **Phase 3**: Implement Split-Screen Local Co-op
4. **Phase 4**: Implement Online Multiplayer
5. **Phase 5**: Create Game Levels
6. **Phase 6**: Configure Project Settings
7. **Phase 7**: Testing

## Key Components

### Blueprints (to be created in Unreal Editor)

- `BP_MultiplayerGameMode` - Manages game rules and player spawning
- `BP_PlayerCharacter` - Third-person character with mannequin mesh
- `BP_MultiplayerController` - Handles player input
- `BP_MultiplayerGameInstance` - Manages sessions and split-screen
- `WBP_MainMenu` - Main menu UI with Host/Join buttons

### Levels (to be created in Unreal Editor)

- `MAP_MainMenu` - Main menu level with UI
- `MAP_Multiplayer` - Main gameplay level with Player Start points

## Configuration

### Enabled Plugins

- **OnlineSubsystem** - Core multiplayer networking
- **OnlineSubsystemNull** - LAN/local multiplayer testing
- **OnlineSubsystemUtils** - Utility functions for online features

### Network Settings

- Default Platform Service: Null (for LAN testing)
- Net Server Max Tick Rate: 60
- Max Net Tick Rate: 60

## Testing Multiplayer

### Split-Screen Local Co-op

1. Play → Advanced Settings
2. Set "Number of Players" to 2
3. Set "Net Mode" to "Play As Listen Server"
4. Click Play

### Online Multiplayer

1. Launch 2 editor instances
2. Instance 1: Click Play (Host)
3. Instance 2: Console command: `open 127.0.0.1`

## Troubleshooting

### Build Errors After Adding C++

If you encounter build errors:

1. Delete `Binaries/`, `Intermediate/`, and `Saved/` folders
2. Right-click `.uproject` → Generate Visual Studio project files
3. Rebuild in Visual Studio

### Mannequin Assets Not Found

- Add Third Person content from Epic Games Launcher
- Or create a Third Person template project and migrate assets

### Split-Screen Not Working

- Verify `BP_MultiplayerGameInstance` has "Create Player" node
- Check PIE settings: "Number of Players" = 2
- Ensure Game Instance Class is set in Project Settings

## Next Steps

After completing the implementation guide:

- Add gameplay mechanics (objectives, scoring, etc.)
- Create additional characters or character customization
- Implement voice chat or text chat
- Add matchmaking UI with session browser
- Deploy to Epic Online Services for internet multiplayer
- Package and distribute the game

## Resources

- [Unreal Engine Multiplayer Documentation](https://docs.unrealengine.com/5.0/en-US/multiplayer-programming-quick-start-for-unreal-engine/)
- [Online Subsystem Overview](https://docs.unrealengine.com/5.0/en-US/online-subsystem-in-unreal-engine/)
- [Blueprint Visual Scripting](https://docs.unrealengine.com/5.0/en-US/blueprints-visual-scripting-in-unreal-engine/)

## Contributing

This is a personal learning/development project. Feel free to fork and experiment!

## License

This project is for educational purposes. Unreal Engine is subject to Epic Games' license terms.

## Author

antoine1anthony

---

**Ready to build multiplayer games? Follow the `MULTIPLAYER_IMPLEMENTATION_GUIDE.md` to get started!**
