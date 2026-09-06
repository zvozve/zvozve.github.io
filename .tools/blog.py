# -*- coding: utf-8 -*-
"""
博客一键操作脚本（逻辑集中在此，方便修改；VSCode tasks.json 只负责调用它）。

参考 source/_posts/hexo/Hexo部署.md「备份」一节的标准流程：
    先备份源码(git) -> 再刷新页面(hexo deploy)

子命令:
  publish   完整流程: git add -> commit -> push hexo -> hexo clean -> generate -> deploy
            可附带提交说明: python .tools/blog.py publish "本次改动说明"
  save      仅备份源码: git add -> commit -> push origin hexo
  build     仅生成静态页: hexo clean + generate
  deploy    仅发布页面: hexo deploy  (推 public/ 到 master 分支 = GitHub Pages)
  preview   本地预览: hexo server  -> http://localhost:4000
  check     检查 front-matter 缺失字段 (.tools/fix_front_matter.py --check)

说明:
  - hexo deploy / git push 需要访问 github.com。本机走 SOCKS5 代理时改下面 PROXY 常量；
    若已配好 git 全局 http.proxy，则此处兜底不生效也无妨。
  - git 首次推送会弹凭据框：选 manager，密码填 GitHub Personal Access Token（不是登录密码）。
"""
import os
import sys
import subprocess

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .tools 上级 = 仓库根
TOOLS = os.path.join(REPO, ".tools")
PROXY = "socks5://127.0.0.1:7897"  # 改代理端口在这里；留空字符串 "" 表示不设置


def run(cmd):
    print(">> " + cmd)
    env = os.environ.copy()
    if PROXY:  # 兜底注入代理，保证 deploy/commit 走代理
        for k in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"):
            if k not in env:
                env[k] = PROXY
    rc = subprocess.run(cmd, shell=True, cwd=REPO, env=env).returncode
    if rc != 0:
        print("[ERROR] 退出码: %d" % rc)
    return rc


def _git_dirty():
    """工作区是否有未提交改动（含未跟踪文件）。"""
    return bool(subprocess.run("git status --porcelain",
                               shell=True, cwd=REPO,
                               capture_output=True, text=True).stdout.strip())


def save(msg="source update"):
    """仅备份源码到 hexo 分支。"""
    run("git add -A")
    if not _git_dirty():
        print("[INFO] 源码无改动，跳过 commit")
        return 0
    run('git commit -m "%s"' % msg)
    return run("git push origin hexo")


def build():
    """仅生成静态页面到 public/。"""
    run("hexo clean")
    return run("hexo generate")


def deploy():
    """仅发布页面（public/ -> master 分支）。"""
    return run("hexo deploy")


def publish(msg="source update"):
    """完整流程：备份源码 + 刷新页面。"""
    print("===== [1/3] 备份源码到 hexo 分支 =====")
    save(msg)
    print("===== [2/3] 生成静态页面 =====")
    build()
    print("===== [3/3] 发布到 GitHub Pages (master) =====")
    return deploy()


def preview():
    return run("hexo server")


def check():
    return run('python "%s" --check' % os.path.join(TOOLS, "fix_front_matter.py"))


CMDS = {
    "publish": publish,
    "save": save,
    "build": build,
    "deploy": deploy,
    "preview": preview,
    "check": check,
}


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in CMDS:
        print("用法: python .tools/blog.py {%s} [提交说明]" % "|".join(CMDS))
        sys.exit(2)
    cmd = sys.argv[1]
    msg = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "source update"
    sys.exit(CMDS[cmd](msg) if cmd in ("publish", "save") else CMDS[cmd]())
