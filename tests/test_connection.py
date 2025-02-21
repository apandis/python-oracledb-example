import unittest
from dotenv import load_dotenv
from src.main import connect_to_oracle

load_dotenv()


class TestOracleConnection(unittest.TestCase):
    def test_connection(self):
        conn, cursor = connect_to_oracle()
        self.assertIsNotNone(conn, "Failed to connect to the Oracle database.")
        if conn:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    unittest.main()
