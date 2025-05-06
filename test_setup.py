import unittest
import os
import sys
import subprocess
import tempfile
import shutil

class SetupScriptTestCase(unittest.TestCase):
    """Test case for setup scripts."""
    
    def setUp(self):
        """Set up test environment."""
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        
        # Copy necessary files to the test directory
        shutil.copy(os.path.join(os.getcwd(), 'requirements.txt'), self.test_dir)
        shutil.copy(os.path.join(os.getcwd(), 'setup.sh'), self.test_dir)
        shutil.copy(os.path.join(os.getcwd(), 'setup.bat'), self.test_dir)
        
        # Make setup.sh executable
        os.chmod(os.path.join(self.test_dir, 'setup.sh'), 0o755)
        
        # Save current directory
        self.original_dir = os.getcwd()
        
        # Change to test directory
        os.chdir(self.test_dir)
    
    def tearDown(self):
        """Clean up after tests."""
        # Change back to original directory
        os.chdir(self.original_dir)
        
        # Remove test directory
        shutil.rmtree(self.test_dir)
    
    def test_requirements_file_exists(self):
        """Test that requirements.txt exists."""
        self.assertTrue(os.path.exists('requirements.txt'))
    
    def test_setup_sh_exists(self):
        """Test that setup.sh exists."""
        self.assertTrue(os.path.exists('setup.sh'))
    
    def test_setup_bat_exists(self):
        """Test that setup.bat exists."""
        self.assertTrue(os.path.exists('setup.bat'))
    
    def test_requirements_content(self):
        """Test that requirements.txt contains expected libraries."""
        with open('requirements.txt', 'r') as f:
            content = f.read()
        
        required_libraries = [
            'Flask',
            'flask-mongoengine',
            'boto3',
            'python-dotenv',
            'Werkzeug'
        ]
        
        for lib in required_libraries:
            self.assertIn(lib, content)
    
    def test_setup_sh_content(self):
        """Test that setup.sh contains expected commands."""
        with open('setup.sh', 'r') as f:
            content = f.read()
        
        expected_commands = [
            'python3 -m venv venv',
            'source venv/bin/activate',
            'pip install -r requirements.txt'
        ]
        
        for cmd in expected_commands:
            self.assertIn(cmd, content)
    
    def test_setup_bat_content(self):
        """Test that setup.bat contains expected commands."""
        with open('setup.bat', 'r') as f:
            content = f.read()
        
        expected_commands = [
            'python -m venv venv',
            'venv\\Scripts\\activate',
            'pip install -r requirements.txt'
        ]
        
        for cmd in expected_commands:
            self.assertIn(cmd, content)

if __name__ == '__main__':
    unittest.main()