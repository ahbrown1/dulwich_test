from dulwich.client import get_transport_and_path
from dulwich.repo import Repo
import pdb
import sys

pdb.set_trace()

repo = Repo(".")

sha = '43543ae87e46d9d258f9cf332fefff306843b734'
sha = '43543ae87e46d9d258f9cf332fefff306843b734'
sha = sys.argv[1]

havit = '0126f7e05058c432eba6852ac402bbb7f841654e'
have = [havit]
want=[sha]
osi = repo.object_store.generate_pack_contents(have, want)
for objs in osi :
     print objs


