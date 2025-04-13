# -----------------------------------------------
# ReNewTech Solutions - Python Starter Template
# -----------------------------------------------

# ✅ Fix SSL verification for external dataset downloads
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# ✅ Core Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings

# ✅ Data Science Libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize, StandardScaler
from sklearn.utils.class_weight import compute_sample_weight
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
from sklearn.svm import LinearSVC

# ✅ Optional: Plotting Settings
plt.rcParams['figure.figsize'] = (10, 6)

# ✅ Turn off warnings for cleaner output
warnings.filterwarnings('ignore')

# ✅ Startup Message
print("🚀 Environment ready: SSL fix applied")
print("\n📚 Libraries imported:")
print("- Pandas")
print("- NumPy")
print("- Matplotlib")
print("- Scikit-learn")
print("\n✅ Ready for Machine Learning or Data Science Work!\n")
