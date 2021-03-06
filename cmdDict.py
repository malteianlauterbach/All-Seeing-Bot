import commands.data_tweaking
import commands.Help
import commands.moderation_tools
import commands.fun

cmdDict = {
	'muteduration': commands.data_tweaking.set_duration,
	'offenseduration': commands.data_tweaking.offense_time,
	'offenselimit': commands.data_tweaking.offense_limit,
	'help': commands.Help.Help,
	'reset': commands.data_tweaking.reset,
	'read': commands.data_tweaking.Read,
	'write': commands.data_tweaking.Write,
	'ban': commands.moderation_tools.ban,
	'unban': commands.moderation_tools.unban,
	'phraselimit': commands.data_tweaking.phrase_limit,
	'muteincrement': commands.data_tweaking.mute_increment,
	'emojimax': commands.data_tweaking.emoji_max,
	'mentionlimit': commands.data_tweaking.mention_limit,
	'actionlog': commands.data_tweaking.action_channel,
	'trust': commands.data_tweaking.test_trust,
	'trustrole': commands.data_tweaking.trust_role,
	'untrustrole': commands.data_tweaking.untrust_role,
	'kick': commands.moderation_tools.kick,
	'mute': commands.moderation_tools.mute,
	'unmute': commands.moderation_tools.unmute,
	'warn': commands.moderation_tools.warn,
	'warns': commands.moderation_tools.get_warns,
	'warnings': commands.moderation_tools.get_warns,
	'removewarn': commands.moderation_tools.remove_warn,
	'modmail': commands.data_tweaking.mail_channel,
	'muterole': commands.data_tweaking.mute_role,
	'exec': commands.data_tweaking.Execute,
	'execute': commands.data_tweaking.Execute,
	'roll': commands.fun.roll,
	'statroll': commands.fun.statroll
}
