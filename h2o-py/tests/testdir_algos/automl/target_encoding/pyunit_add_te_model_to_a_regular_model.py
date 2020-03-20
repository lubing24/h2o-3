from __future__ import print_function
import sys, os

sys.path.insert(1, os.path.join("..","..","..",".."))
import h2o
from tests import pyunit_utils
from h2o.estimators import H2OTargetEncoderEstimator
from h2o.estimators.gbm import H2OGradientBoostingEstimator
from h2o.exceptions import H2OTypeError
import unittest


def test_target_encoder_attached_as_preprocessor():
    print("Check that attached TargetEncoderModel is being used during training and scoring")
    targetColumnName = "survived"
    foldColumnName = "kfold_column"

    teColumns = ["cabin", "embarked"]
    trainingFrame = h2o.import_file(pyunit_utils.locate("smalldata/gbm_test/titanic.csv"), header=1)

    trainingFrame[targetColumnName] = trainingFrame[targetColumnName].asfactor()
    trainingFrame[foldColumnName] = trainingFrame.kfold_column(n_folds=5, seed=1234)

    te = H2OTargetEncoderEstimator(k = 0.7, f = 0.3, data_leakage_handling = "KFold", fold_column=foldColumnName)
    te.train(training_frame=trainingFrame, x=teColumns, y=targetColumnName)
    print(te)
    print(trainingFrame)

    myX = ["pclass", "sex", "age", "sibsp", "parch", "fare", "cabin", "embarked", "home.dest"]
    titanic_gbm_model = H2OGradientBoostingEstimator(ntrees=50,
                                             learn_rate=0.1,
                                             score_tree_interval=10,
                                             stopping_rounds=5,
                                             stopping_metric="AUC",
                                             stopping_tolerance=0.001,
                                             distribution="multinomial",
                                             categorical_encoding="enum_limited",
                                             te_model = te,
                                             seed=1234)

    assert titanic_gbm_model.te_model is not None

    titanic_gbm_model.train(x=myX, y=targetColumnName,
                    training_frame=trainingFrame)

    variable_importance = titanic_gbm_model._model_json['output']['variable_importances'].as_data_frame()

    print(variable_importance)
    # Checking that model used te encoded columns during training
    var_imp_for_te_encoded_columns = variable_importance[variable_importance['variable'].str.contains('_te', regex=True)]
    print(var_imp_for_te_encoded_columns)
    assert len(var_imp_for_te_encoded_columns) == 2

    # Checking that predictions are different when we attach te model
    preds = titanic_gbm_model.predict(trainingFrame)
    print(preds)

    # Let' train basically the same Model but without te_model_key
    titanic_gbm_model_without_te = H2OGradientBoostingEstimator(ntrees=50,
                                                     learn_rate=0.1,
                                                     score_tree_interval=10,
                                                     stopping_rounds=5,
                                                     stopping_metric="AUC",
                                                     stopping_tolerance=0.001,
                                                     distribution="multinomial",
                                                     categorical_encoding="enum_limited",
                                                     seed=1234)

    assert titanic_gbm_model_without_te.te_model is None

    titanic_gbm_model_without_te.train(x=myX, y=targetColumnName,
                            training_frame=trainingFrame)

    preds_without_te = titanic_gbm_model_without_te.predict(trainingFrame)
    print(preds_without_te)

    assert not pyunit_utils.compare_frames_local(preds, preds_without_te, 1, tol=1e-10, returnResult=True), "Predictions should be different"


def test_target_encoder_could_be_passed_by_key_of_the_model():
  print("Check that TargetEncoderModel could be passed as key")
  targetColumnName = "survived"
  foldColumnName = "kfold_column"

  teColumns = ["cabin", "embarked"]
  trainingFrame = h2o.import_file(pyunit_utils.locate("smalldata/gbm_test/titanic.csv"), header=1)

  trainingFrame[targetColumnName] = trainingFrame[targetColumnName].asfactor()
  trainingFrame[foldColumnName] = trainingFrame.kfold_column(n_folds=5, seed=1234)

  te = H2OTargetEncoderEstimator(k = 0.7, f = 0.3, data_leakage_handling = "KFold", fold_column=foldColumnName)
  te.train(training_frame=trainingFrame, x=teColumns, y=targetColumnName)

  myX = ["pclass", "sex", "age", "sibsp", "parch", "fare", "cabin", "embarked", "home.dest"]
  titanic_gbm_model = H2OGradientBoostingEstimator(ntrees=50,
                                                   learn_rate=0.1,
                                                   score_tree_interval=10,
                                                   stopping_rounds=5,
                                                   stopping_metric="AUC",
                                                   stopping_tolerance=0.001,
                                                   distribution="multinomial",
                                                   categorical_encoding="enum_limited",
                                                   te_model = te.model_id,
                                                   seed=1234)

  assert titanic_gbm_model.te_model is not None

  titanic_gbm_model.train(x=myX, y=targetColumnName,
                          training_frame=trainingFrame)

  variable_importance = titanic_gbm_model._model_json['output']['variable_importances'].as_data_frame()

  print(variable_importance)
  # Checking that model used te encoded columns during training
  var_imp_for_te_encoded_columns = variable_importance[variable_importance['variable'].str.contains('_te', regex=True)]
  print(var_imp_for_te_encoded_columns)
  assert len(var_imp_for_te_encoded_columns) == 2


def test_only_te_model_could_be_added_as_preprocessor():
  print("Check that only TargetEncoderModel could be assigned to te_model argument in Py API ( as a key it is possible though)")
  targetColumnName = "survived"
  foldColumnName = "kfold_column"

  trainingFrame = h2o.import_file(pyunit_utils.locate("smalldata/gbm_test/titanic.csv"), header=1)

  trainingFrame[targetColumnName] = trainingFrame[targetColumnName].asfactor()
  trainingFrame[foldColumnName] = trainingFrame.kfold_column(n_folds=5, seed=1234)

  myX = ["pclass", "sex", "age", "sibsp", "parch", "fare", "cabin", "embarked", "home.dest"]

  gbm_preprocessor_model = H2OGradientBoostingEstimator(ntrees=50,
                                                   learn_rate=0.1,
                                                   score_tree_interval=10,
                                                   stopping_rounds=5,
                                                   stopping_metric="AUC",
                                                   stopping_tolerance=0.001,
                                                   distribution="multinomial",
                                                   categorical_encoding="enum_limited",
                                                   seed=1234)

  gbm_preprocessor_model.train(x=myX, y=targetColumnName,
                          training_frame=trainingFrame)


  # Checking that assigning NOT a te model causes validation error
  with unittest.TestCase.assertRaises(None, H2OTypeError) as err:
    H2OGradientBoostingEstimator(ntrees=50,
                                 learn_rate=0.1,
                                 score_tree_interval=10,
                                 stopping_rounds=5,
                                 stopping_metric="AUC",
                                 stopping_tolerance=0.001,
                                 distribution="multinomial",
                                 categorical_encoding="enum_limited",
                                 te_model = gbm_preprocessor_model,
                                 seed=1234)
  assert "Argument `te_model` should be a None | string | H2OTargetEncoderEstimator, got H2OGradientBoostingEstimator" \
         in str(err.exception), "Validation should not allow non-targetencoder model for `te_model` parameter"


testList = [
    test_target_encoder_attached_as_preprocessor,
    test_target_encoder_could_be_passed_by_key_of_the_model,
    test_only_te_model_could_be_added_as_preprocessor
]

pyunit_utils.run_tests(testList)
