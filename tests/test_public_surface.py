import json, subprocess, sys, tempfile, unittest
from pathlib import Path

SCRIPT=Path(__file__).resolve().parents[1]/"tools"/"check_public_surface.py"
class PublicSurfaceTests(unittest.TestCase):
    def run_case(self, payload):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"record.json"; p.write_text(json.dumps(payload),encoding="utf-8")
            return subprocess.run([sys.executable,str(SCRIPT),td],text=True,capture_output=True)
    def test_clean_passes(self):
        r=self.run_case({"subject_id":"system-001","validity_state":"QUESTIONED"})
        self.assertEqual(r.returncode,0); self.assertEqual(r.stdout.strip(),"PASS")
    def test_protected_field_fails_without_echo(self):
        marker="private-source-do-not-echo"
        r=self.run_case({"reporter_identity":marker})
        self.assertEqual(r.returncode,1); self.assertIn("PROTECTED_CONCERN_FIELD",r.stdout); self.assertNotIn(marker,r.stdout)
if __name__=="__main__": unittest.main()
