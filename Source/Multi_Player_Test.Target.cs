using UnrealBuildTool;
using System.Collections.Generic;

public class Multi_Player_TestTarget : TargetRules
{
	public Multi_Player_TestTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Game;
		DefaultBuildSettings = BuildSettingsVersion.V5;
		IncludeOrderVersion = EngineIncludeOrderVersion.Unreal5_6;
		ExtraModuleNames.Add("Multi_Player_Test");
	}
}


