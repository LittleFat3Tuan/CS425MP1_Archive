import unittest
import io
import client
import asyncio
import sys


class TestLogSys(unittest.TestCase):
    def test_case1(self):
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        asyncio.get_event_loop().run_until_complete(client.main_logic('grep -c "I love" ../test_logs/*c1.log'))

        output = new_stdout.getvalue()

        sys.stdout = old_stdout

        ans = ''
        for i in range(10):
            ans = ans + f'../test_logs/test_log_m{i+1}c1.log:34200\n\n'

        self.assertEqual(output, ans)

    def test_case2(self):
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        asyncio.get_event_loop().run_until_complete(client.main_logic('grep -c "I love" ../test_logs/*c2.log'))

        output = new_stdout.getvalue()

        sys.stdout = old_stdout

        ans = ''
        for i in range(4):
            ans = ans + f'../test_logs/test_log_m{i+1}c2.log:34200\n\n'

        self.assertEqual(output, ans)
    
    def test_case3(self):
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        asyncio.get_event_loop().run_until_complete(client.main_logic('grep -c "I love" ../test_logs/*c3.log'))

        output = new_stdout.getvalue()

        sys.stdout = old_stdout

        ans = ''
        for i in range(1):
            ans = ans + f'../test_logs/test_log_m{i+1}c3.log:34200\n\n'

        self.assertEqual(output, ans)
    
    def test_case4(self):
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        asyncio.get_event_loop().run_until_complete(client.main_logic('grep -c "I love" ../test_logs/*c4.log'))

        output = new_stdout.getvalue()

        sys.stdout = old_stdout

        ans = ''
        for i in range(10):
            ans = ans + f'../test_logs/test_log_m{i+1}c4.log:4800\n\n'

        self.assertEqual(output, ans)
    
    def test_case5(self):
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        asyncio.get_event_loop().run_until_complete(client.main_logic('grep -c "I love" ../test_logs/*c5.log'))

        output = new_stdout.getvalue()

        sys.stdout = old_stdout

        ans = ''
        for i in range(4):
            ans = ans + f'../test_logs/test_log_m{i+1}c5.log:4800\n\n'

        self.assertEqual(output, ans)
    
    def test_case6(self):
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        asyncio.get_event_loop().run_until_complete(client.main_logic('grep -c "I love" ../test_logs/*c6.log'))

        output = new_stdout.getvalue()

        sys.stdout = old_stdout

        ans = ''
        for i in range(1):
            ans = ans + f'../test_logs/test_log_m{i+1}c6.log:4800\n\n'

        self.assertEqual(output, ans)
    
    def test_case7(self):
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        asyncio.get_event_loop().run_until_complete(client.main_logic('grep -c "I love" ../test_logs/*c7.log'))

        output = new_stdout.getvalue()

        sys.stdout = old_stdout

        ans = ''
        for i in range(10):
            ans = ans + f'../test_logs/test_log_m{i+1}c7.log:300\n\n'

        self.assertEqual(output, ans)
    
    def test_case8(self):
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        asyncio.get_event_loop().run_until_complete(client.main_logic('grep -c "I love" ../test_logs/*c8.log'))

        output = new_stdout.getvalue()

        sys.stdout = old_stdout

        ans = ''
        for i in range(4):
            ans = ans + f'../test_logs/test_log_m{i+1}c8.log:300\n\n'

        self.assertEqual(output, ans)
    
    def test_case9(self):
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        asyncio.get_event_loop().run_until_complete(client.main_logic('grep -c "I love" ../test_logs/*c9.log'))

        output = new_stdout.getvalue()

        sys.stdout = old_stdout

        ans = ''
        for i in range(1):
            ans = ans + f'../test_logs/test_log_m{i+1}c9.log:300\n\n'

        self.assertEqual(output, ans)


if __name__ == '__main__':
    unittest.main()




