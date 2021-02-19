# File created by Utkarsh Gupta
# Dated 15/1/2020

# Touched on 17/1/2020 by Utkarsh Gupta

# Tree Class : AI model to test our thesis.

# libraries
from tensorflow_estimator.python.estimator.canned.boosted_trees import BoostedTreesClassifier
from tensorflow_estimator.python.estimator.inputs.pandas_io import pandas_input_fn
from tensorflow import feature_column
from tensorflow import saved_model
import tensorflow as tf
import pandas as pd
import numpy


class treeClassifier:
    def __init__(self):
        self.featureList = ("itching","skin_rash","nodal_skin_eruptions","continuous_sneezing","shivering","chills",
                            "joint_pain","stomach_pain","acidity","ulcers_on_tongue","muscle_wasting","vomiting",
                            "burning_micturition","spotting_ urination","fatigue","weight_gain","anxiety",
                            "cold_hands_and_feets","mood_swings","weight_loss","restlessness","lethargy",
                            "patches_in_throat","irregular_sugar_level","cough","high_fever","sunken_eyes",
                            "breathlessness","sweating","dehydration","indigestion","headache","yellowish_skin",
                            "dark_urine","nausea","loss_of_appetite","pain_behind_the_eyes","back_pain","constipation",
                            "abdominal_pain","diarrhoea","mild_fever","yellow_urine","yellowing_of_eyes",
                            "acute_liver_failure","swelling_of_stomach","swelled_lymph_nodes",
                            "malaise","blurred_and_distorted_vision","phlegm","throat_irritation","redness_of_eyes",
                            "sinus_pressure","runny_nose","congestion","chest_pain","weakness_in_limbs",
                            "fast_heart_rate","pain_during_bowel_movements","pain_in_anal_region","bloody_stool",
                            "irritation_in_anus","neck_pain","dizziness","cramps","bruising","obesity","swollen_legs",
                            "swollen_blood_vessels","puffy_face_and_eyes","enlarged_thyroid","brittle_nails",
                            "swollen_extremeties","excessive_hunger","extra_marital_contacts",
                            "drying_and_tingling_lips","slurred_speech","knee_pain","hip_joint_pain",'muscle_weakness',
                            "stiff_neck","swelling_joints","movement_stiffness","spinning_movements","loss_of_balance",
                            "unsteadiness","weakness_of_one_body_side","loss_of_smell","bladder_discomfort",
                            "foul_smell_of urine","continuous_feel_of_urine","passage_of_gases","internal_itching",
                            "toxic_look_(typhos)","depression","irritability","muscle_pain","altered_sensorium",
                            "red_spots_over_body","belly_pain","abnormal_menstruation","dischromic _patches",
                            "watering_from_eyes","increased_appetite","polyuria","family_history","mucoid_sputum",
                            "rusty_sputum","lack_of_concentration","visual_disturbances","receiving_blood_transfusion",
                            "receiving_unsterile_injections","coma","stomach_bleeding","distention_of_abdomen",
                            "history_of_alcohol_consumption","fluid_overload","blood_in_sputum",
                            "prominent_veins_on_calf","palpitations","painful_walking","pus_filled_pimples",
                            "blackheads","scurring","skin_peeling","silver_like_dusting","small_dents_in_nails",
                            "inflammatory_nails","blister","red_sore_around_nose","yellow_crust_ooze")
        self.diseases = ["Fungal infection","Allergy","GERD","Chronic cholestasis","Drug Reaction","Peptic ulcer diseae",
                         "AIDS","Diabetes","Gastroenteritis","Bronchial Asthma","Hypertension","Migraine",
                         "Cervical spondylosis","Paralysis (brain hemorrhage)","Jaundice","Malaria","Chicken pox",
                         "Dengue","Typhoid","hepatitis A","Hepatitis B","Hepatitis C","Hepatitis D","Hepatitis E",
                         "Alcoholic hepatitis","Tuberculosis","Common Cold","Pneumonia","Dimorphic hemmorhoids(piles)",
                         "Heart attack","Varicose veins","Hypothyroidism","Hyperthyroidism","Hypoglycemia",
                         "Osteoarthristis","Arthritis","(vertigo) Paroymsal  Positional Vertigo","Acne",
                         "Urinary tract infection","Psoriasis","Impetigo","prognosis"]
        # Fixed Tree arguments
        self.featureColumn = list()
        self.n_classes = len(self.diseases)
        self.weight_column = None
        self.label_vocabulary = None
        self.min_node_weight = 0.0
        self.config = None
        self.center_bias = False
        self.pruning_mode = 'none'
        self.quantile_sketch_epsilon = 0.01
        self.train_in_memory = False
        self.symptomList = None
        self.model_dir = "./Model Temp Files/"
        self.savedTreeLocation = './Saved model\\1613754500'
        # Changeable Tree arguments for structure
        self.n_trees = 100
        self.max_depth = 6
        self.learning_rate = 0.1
        self.n_batches_per_layer = 1
        # Changeable Tree arguments for Over-fitting
        self.l1_regularization = 0.0
        self.l2_regularization = 0.0
        self.tree_complexity = 0.0
        # Data
        self.trainingData = None
        self.testingData = None
        self.trainX = None
        self.trainY = None
        self.testX = None
        self.testY = None
        # Tree
        self.tree = None
        self.importedTree = None
        # Evaluation matrix of Tree
        self.evaluationMatrix = None

    def getParameterList(self, noOfTree, maxTreeDepth, learningRate, noOfBatchesPerLayer):
        self.n_trees = noOfTree
        self.max_depth = maxTreeDepth
        self.learning_rate = learningRate
        self.n_batches_per_layer = noOfBatchesPerLayer

    def loadFiles(self):
        self.trainingData = pd.read_csv("./dataset/training_data.csv")
        self.testingData = pd.read_csv("./dataset/test_data.csv")
        self.trainX = self.trainingData.iloc[:, :131]
        self.trainY = self.trainingData.iloc[:, 131:]
        self.testX = self.testingData.iloc[:, :131]
        self.testY = self.testingData.iloc[:, 131:]

    def generateFeatureColumn(self):
        for columnName in self.featureList:
            if columnName != "prognosis":
                self.featureColumn.append(feature_column.categorical_column_with_identity(key=columnName,
                                                                                          num_buckets=2))
            else:
                self.featureColumn.append((feature_column.categorical_column_with_identity(key=columnName,
                                                                                           num_buckets=41)))

    def constructTree(self):
        self.tree = BoostedTreesClassifier(self.featureColumn, self.n_batches_per_layer, self.model_dir, self.n_classes,
                                           self.weight_column, self.label_vocabulary, self.n_trees, self.max_depth,
                                           self.learning_rate, self.l1_regularization, self.l2_regularization,
                                           self.tree_complexity, self.min_node_weight, self.config, self.center_bias,
                                           self.pruning_mode, self.quantile_sketch_epsilon, self.train_in_memory)

    def trainingInputFunction(self):
        return pandas_input_fn(self.trainX, self.trainY['prognosis'], batch_size=128, num_epochs=1, shuffle=True,
                               num_threads=1)

    def testingInputFunction(self):
        return pandas_input_fn(self.testX, self.testY['prognosis'], batch_size=128, num_epochs=1, shuffle=False,
                               num_threads=1)

    def trainTree(self):
        self.tree.train(self.trainingInputFunction(), hooks=None, steps=None, max_steps=None, saving_listeners=None)

    def evaluateTree(self):
        self.evaluationMatrix = self.tree.evaluate(self.testingInputFunction(), steps=None, hooks=None,
                                                   checkpoint_path=None, name=None)
        print(self.evaluationMatrix)

    def saveTreeModel(self):
        inputFn = tf.estimator.export.build_parsing_serving_input_receiver_fn(
            tf.feature_column.make_parse_example_spec(self.featureColumn))
        self.tree.export_saved_model("./Saved model", inputFn)

    def loadTreeModel(self):
        self.loadFiles()
        print("files loaded")
        if saved_model.contains_saved_model(self.savedTreeLocation):
            self.importedTree = saved_model.load(self.savedTreeLocation)
            result = self.predict2(self.testX, self.importedTree)
            print("Tree loaded...", result)
        else:
            print("Tree not available.")

    def predict2(self, dfeval, importedModel):
        colNames = dfeval.columns
        dtypes = dfeval.dtypes
        predictions = []
        for row in dfeval.iterrows():
            example = tf.train.Example()
            for i in range(len(colNames)):
                dtype = dtypes[i]
                colName = colNames[i]
                value = row[1][colName]
                if dtype == "object":
                    value = bytes(value, "utf-8")
                    example.features.feature[colName].bytes_list.value.extend([value])
                elif dtype == "float":
                    example.features.feature[colName].float_list.value.extend([value])
                elif dtype == "int":
                    example.features.feature[colName].int64_list.value.extend([value])
            predictions.append(
                importedModel.signatures["predict"](
                    examples=tf.constant([example.SerializeToString()])))

        return predictions

    def predictDisease(self, symptomList):
        symptomList = pd.DataFrame([symptomList], columns=self.featureList)
        input_fn = pandas_input_fn(symptomList, None, batch_size=1, num_epochs=1, shuffle=False,
                                   num_threads=1)
        prediction = self.tree.predict(input_fn, predict_keys=None, hooks=None, checkpoint_path=None,
                                       yield_single_examples=True)
        disease = numpy.argmax(list(prediction)[0]['logits'])
        return self.diseases[int(disease)]
