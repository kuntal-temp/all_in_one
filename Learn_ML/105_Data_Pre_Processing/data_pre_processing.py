# Importing the dataset
dataset = pd.read_csv('Iris.csv')

# View Raw Data
print(dataset.head(10))
print(dataset.info())
print(dataset.describe())

# Dividing data into X and y
X = dataset.iloc[:, 1:5].values
y = dataset.iloc[:, -1].values

# Taking care of missing data
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
X[:, :] = imputer.fit_transform(X[:, :])

# Encoding Independent categorical data
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [5])], remainder='passthrough')
X = ct.fit_transform(X)

# Label Encoding
le = LabelEncoder()
y = le.fit_transform(y)

# Training Test Spliting
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)

# Feature Scaling
sc_x = StandardScaler()
X_train[:, 3:] = sc_x.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc_x.fit_transform(X_test[:, 3:])

sc_y = StandardScaler()
Y_train = Y_train.reshape(-1,1)
Y_test = Y_test.reshape(-1,1)

Y_train[:, :] = sc_y.fit_transform(Y_train[:, :])
Y_test[:, :] = sc_y.fit_transform(Y_test[:, :])

Y_train = Y_train.flatten(order='C')
Y_test = Y_test.flatten(order='C')
