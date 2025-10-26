using UnrealBuildTool;
using System.Collections.Generic;

public class Multi_Player_TestEditorTarget : TargetRules
{
	public Multi_Player_TestEditorTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Editor;
		DefaultBuildSettings = BuildSettingsVersion.V5;
		IncludeOrderVersion = EngineIncludeOrderVersion.Unreal5_6;
		ExtraModuleNames.Add("Multi_Player_Test");
	}
}


