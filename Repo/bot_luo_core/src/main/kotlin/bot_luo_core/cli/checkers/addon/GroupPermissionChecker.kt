package bot_luo_core.cli.checkers.addon

import bot_luo_core.cli.Checker
import bot_luo_core.cli.CmdContext
import bot_luo_core.cli.CmdExecutable
import bot_luo_core.data.PmsGroups.readPmsOn

class GroupPermissionChecker: Checker {

    override val name = "群组权限检定器"

    override fun check(cmd: CmdExecutable, context: CmdContext) {
        val p = context.group.pmsGroup
        val i = p.readPmsOn(cmd)
        if (i <= 0) throw CheckerFatal("群组权限不足，要求：${cmd.pmsLevel.name} 群组权限：${p.name}($i)")
    }
}