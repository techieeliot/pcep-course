import sys 
import sklearn as scikit

name = input("Enter your name: ")
sys.stdout.write(f'Hello, {name}')

scikit_learn_version = scikit.__version__
print(f"\nscikit-learn version: {scikit_learn_version}")

