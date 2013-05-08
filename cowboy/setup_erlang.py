
import subprocess
import sys
import setup_util

def start(args):
  setup_util.replace_text("cowboy/src/hello_world_app.erl", "\"benchmarkdbpass\", \".*\", 3306", "\"benchmarkdbpass\", \"" + args.database_host + "\", 3306")

  try:
    subprocess.check_call("./rebar get-deps", shell=True, cwd="cowboy")
    subprocess.check_call("./rebar compile", shell=True, cwd="cowboy")
    subprocess.check_call("erl -pa ebin deps/*/ebin -s hello_world -noshell -detached", shell=True, cwd="cowboy")
    return 0
  except subprocess.CalledProcessError:
    return 1
def stop():
  try:
    subprocess.check_call("killall beam.smp", shell=True, cwd="/usr/bin")
    return 0
  except subprocess.CalledProcessError:
    return 1