#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

from h2o.estimators.estimator_base import H2OEstimator
from h2o.estimators.targetencoder import H2OTargetEncoderEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric


class H2OAggregatorEstimator(H2OEstimator):
    """
    Aggregator

    """

    algo = "aggregator"
    param_names = {"model_id", "training_frame", "response_column", "ignored_columns", "ignore_const_cols",
                   "target_num_exemplars", "rel_tol_num_exemplars", "transform", "categorical_encoding",
                   "save_mapping_frame", "num_iteration_without_new_exemplar", "export_checkpoints_dir", "te_model_id"}

    def __init__(self, **kwargs):
        super(H2OAggregatorEstimator, self).__init__()
        self._parms = {}
        for pname, pvalue in kwargs.items():
            if pname == 'model_id':
                self._id = pvalue
                self._parms["model_id"] = pvalue
            elif pname in self.param_names:
                # Using setattr(...) will invoke type-checking of the arguments
                setattr(self, pname, pvalue)
            else:
                raise H2OValueError("Unknown parameter %s = %r" % (pname, pvalue))
        self._parms["_rest_version"] = 99

    @property
    def training_frame(self):
        """
        Id of the training data frame.

        Type: ``H2OFrame``.

        :examples:

        >>> df = h2o.create_frame(rows=10000,
        ...                       cols=10,
        ...                       categorical_fraction=0.6,
        ...                       integer_fraction=0,
        ...                       binary_fraction=0,
        ...                       real_range=100,
        ...                       integer_range=100,
        ...                       missing_fraction=0,
        ...                       factors=100,
        ...                       seed=1234)
        >>> params = {"target_num_exemplars": 1000,
        ...           "rel_tol_num_exemplars": 0.5,
        ...           "categorical_encoding": "eigen",
        ...           "num_iteration_without_new_exemplar": 400}
        >>> agg = H2OAggregatorEstimator(**params)
        >>> agg.train(training_frame=df)
        >>> new_df = agg.aggregated_frame
        >>> new_df
        """
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        self._parms["training_frame"] = H2OFrame._validate(training_frame, 'training_frame')


    @property
    def response_column(self):
        """
        Response variable column.

        Type: ``str``.
        """
        return self._parms.get("response_column")

    @response_column.setter
    def response_column(self, response_column):
        assert_is_type(response_column, None, str)
        self._parms["response_column"] = response_column


    @property
    def ignored_columns(self):
        """
        Names of columns to ignore for training.

        Type: ``List[str]``.
        """
        return self._parms.get("ignored_columns")

    @ignored_columns.setter
    def ignored_columns(self, ignored_columns):
        assert_is_type(ignored_columns, None, [str])
        self._parms["ignored_columns"] = ignored_columns


    @property
    def ignore_const_cols(self):
        """
        Ignore constant columns.

        Type: ``bool``  (default: ``True``).

        :examples:

        >>> df = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip")
        >>> params = {"ignore_const_cols": False,
        ...           "target_num_exemplars": 500,
        ...           "rel_tol_num_exemplars": 0.3,
        ...           "transform": "standardize",
        ...           "categorical_encoding": "eigen"}
        >>> model = H2OAggregatorEstimator(**params)
        >>> model.train(training_frame=df)
        >>> new_df = model.aggregated_frame
        >>> new_df
        """
        return self._parms.get("ignore_const_cols")

    @ignore_const_cols.setter
    def ignore_const_cols(self, ignore_const_cols):
        assert_is_type(ignore_const_cols, None, bool)
        self._parms["ignore_const_cols"] = ignore_const_cols


    @property
    def target_num_exemplars(self):
        """
        Targeted number of exemplars

        Type: ``int``  (default: ``5000``).

        :examples:

        >>> df = h2o.create_frame(rows=10000,
        ...                       cols=10,
        ...                       categorical_fraction=0.6,
        ...                       integer_fraction=0,
        ...                       binary_fraction=0,
        ...                       real_range=100,
        ...                       integer_range=100,
        ...                       missing_fraction=0,
        ...                       factors=100,
        ...                       seed=1234)
        >>> params = {"target_num_exemplars": 1000,
        ...           "rel_tol_num_exemplars": 0.5,
        ...           "categorical_encoding": "eigen",
        ...           "num_iteration_without_new_exemplar": 400}
        >>> agg = H2OAggregatorEstimator(**params)
        >>> agg.train(training_frame=df)
        >>> new_df = agg.aggregated_frame
        >>> new_df
        """
        return self._parms.get("target_num_exemplars")

    @target_num_exemplars.setter
    def target_num_exemplars(self, target_num_exemplars):
        assert_is_type(target_num_exemplars, None, int)
        self._parms["target_num_exemplars"] = target_num_exemplars


    @property
    def rel_tol_num_exemplars(self):
        """
        Relative tolerance for number of exemplars (e.g, 0.5 is +/- 50 percents)

        Type: ``float``  (default: ``0.5``).

        :examples:

        >>> df = h2o.create_frame(rows=10000,
        ...                       cols=10,
        ...                       categorical_fraction=0.6,
        ...                       integer_fraction=0,
        ...                       binary_fraction=0,
        ...                       real_range=100,
        ...                       integer_range=100,
        ...                       missing_fraction=0,
        ...                       factors=100,
        ...                       seed=1234)
        >>> params = {"target_num_exemplars": 1000,
        ...           "rel_tol_num_exemplars": 0.5,
        ...           "categorical_encoding": "eigen",
        ...           "num_iteration_without_new_exemplar": 400}
        >>> agg = H2OAggregatorEstimator(**params)
        >>> agg.train(training_frame=df)
        >>> new_df = agg.aggregated_frame
        >>> new_df
        """
        return self._parms.get("rel_tol_num_exemplars")

    @rel_tol_num_exemplars.setter
    def rel_tol_num_exemplars(self, rel_tol_num_exemplars):
        assert_is_type(rel_tol_num_exemplars, None, numeric)
        self._parms["rel_tol_num_exemplars"] = rel_tol_num_exemplars


    @property
    def transform(self):
        """
        Transformation of training data

        One of: ``"none"``, ``"standardize"``, ``"normalize"``, ``"demean"``, ``"descale"``  (default: ``"normalize"``).

        :examples:

        >>> df = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip")
        >>> params = {"ignore_const_cols": False,
        ...           "target_num_exemplars": 500,
        ...           "rel_tol_num_exemplars": 0.3,
        ...           "transform": "standardize",
        ...           "categorical_encoding": "eigen"}
        >>> model = H2OAggregatorEstimator(**params)
        >>> model.train(training_frame=df)
        >>> new_df = model.aggregated_frame
        """
        return self._parms.get("transform")

    @transform.setter
    def transform(self, transform):
        assert_is_type(transform, None, Enum("none", "standardize", "normalize", "demean", "descale"))
        self._parms["transform"] = transform


    @property
    def categorical_encoding(self):
        """
        Encoding scheme for categorical features

        One of: ``"auto"``, ``"enum"``, ``"one_hot_internal"``, ``"one_hot_explicit"``, ``"binary"``, ``"eigen"``,
        ``"label_encoder"``, ``"sort_by_response"``, ``"enum_limited"``  (default: ``"auto"``).

        :examples:

        >>> df = h2o.create_frame(rows=10000,
        ...                       cols=10,
        ...                       categorical_fraction=0.6,
        ...                       integer_fraction=0,
        ...                       binary_fraction=0,
        ...                       real_range=100,
        ...                       integer_range=100,
        ...                       missing_fraction=0,
        ...                       factors=100,
        ...                       seed=1234)
        >>> params = {"target_num_exemplars": 1000,
        ...           "rel_tol_num_exemplars": 0.5,
        ...           "categorical_encoding": "eigen"}
        >>> agg = H2OAggregatorEstimator(**params)
        >>> agg.train(training_frame=df)
        >>> new_df = agg.aggregated_frame
        >>> new_df
        """
        return self._parms.get("categorical_encoding")

    @categorical_encoding.setter
    def categorical_encoding(self, categorical_encoding):
        assert_is_type(categorical_encoding, None, Enum("auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen", "label_encoder", "sort_by_response", "enum_limited"))
        self._parms["categorical_encoding"] = categorical_encoding


    @property
    def save_mapping_frame(self):
        """
        Whether to export the mapping of the aggregated frame

        Type: ``bool``  (default: ``False``).

        :examples:

        >>> df = h2o.create_frame(rows=10000,
        ...                       cols=10,
        ...                       categorical_fraction=0.6,
        ...                       integer_fraction=0,
        ...                       binary_fraction=0,
        ...                       real_range=100,
        ...                       integer_range=100,
        ...                       missing_fraction=0,
        ...                       factors=100,
        ...                       seed=1234)
        >>> params = {"target_num_exemplars": 1000,
        ...           "rel_tol_num_exemplars": 0.5,
        ...           "categorical_encoding": "eigen",
        ...           "save_mapping_frame": True}
        >>> agg = H2OAggregatorEstimator(**params)
        >>> agg.train(training_frame=df)
        >>> mapping_frame = agg.mapping_frame
        >>> mapping_frame
        """
        return self._parms.get("save_mapping_frame")

    @save_mapping_frame.setter
    def save_mapping_frame(self, save_mapping_frame):
        assert_is_type(save_mapping_frame, None, bool)
        self._parms["save_mapping_frame"] = save_mapping_frame


    @property
    def num_iteration_without_new_exemplar(self):
        """
        The number of iterations to run before aggregator exits if the number of exemplars collected didn't change

        Type: ``int``  (default: ``500``).

        :examples:

        >>> df = h2o.create_frame(rows=10000,
        ...                       cols=10,
        ...                       categorical_fraction=0.6,
        ...                       integer_fraction=0,
        ...                       binary_fraction=0,
        ...                       real_range=100,
        ...                       integer_range=100,
        ...                       missing_fraction=0,
        ...                       factors=100,
        ...                       seed=1234)
        >>> params = {"target_num_exemplars": 1000,
        ...           "rel_tol_num_exemplars": 0.5,
        ...           "categorical_encoding": "eigen",
        ...           "num_iteration_without_new_exemplar": 400}
        >>> agg = H2OAggregatorEstimator(**params)
        >>> agg.train(training_frame=df)
        >>> new_df = agg.aggregated_frame
        >>> new_df
        """
        return self._parms.get("num_iteration_without_new_exemplar")

    @num_iteration_without_new_exemplar.setter
    def num_iteration_without_new_exemplar(self, num_iteration_without_new_exemplar):
        assert_is_type(num_iteration_without_new_exemplar, None, int)
        self._parms["num_iteration_without_new_exemplar"] = num_iteration_without_new_exemplar


    @property
    def export_checkpoints_dir(self):
        """
        Automatically export generated models to this directory.

        Type: ``str``.

        :examples:

        >>> import tempfile
        >>> from os import listdir
        >>> df = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip")
        >>> checkpoints_dir = tempfile.mkdtemp()
        >>> model = H2OAggregatorEstimator(target_num_exemplars=500, 
        ...                                rel_tol_num_exemplars=0.3,
        ...                                export_checkpoints_dir=checkpoints_dir)
        >>> model.train(training_frame=df)
        >>> new_df = model.aggregated_frame
        >>> new_df
        >>> len(listdir(checkpoints_dir))
        """
        return self._parms.get("export_checkpoints_dir")

    @export_checkpoints_dir.setter
    def export_checkpoints_dir(self, export_checkpoints_dir):
        assert_is_type(export_checkpoints_dir, None, str)
        self._parms["export_checkpoints_dir"] = export_checkpoints_dir


    @property
    def te_model_id(self):
        """
        Key of H2OTargetEncoderEstimator or H2OTargetEncoderEstimator

        Type: ``str`` | ``H2OTargetEncoderEstimator``.
        """
        return self._parms.get("te_model_id")

    @te_model_id.setter
    def te_model_id(self, te_model_id):
        assert_is_type(te_model_id, None, str, H2OTargetEncoderEstimator)
        self._parms["te_model_id"] = te_model_id.key if isinstance(te_model_id, H2OTargetEncoderEstimator) else te_model_id


    @property
    def aggregated_frame(self):
        if (self._model_json is not None
                and self._model_json.get("output", {}).get("output_frame", {}).get("name") is not None):
            out_frame_name = self._model_json["output"]["output_frame"]["name"]
            return H2OFrame.get_frame(out_frame_name)

    @property
    def mapping_frame(self):
        if self._model_json is None:
            return None
        mj = self._model_json
        if mj.get("output", {}).get("mapping_frame", {}).get("name") is not None:
            mapping_frame_name = mj["output"]["mapping_frame"]["name"]
            return H2OFrame.get_frame(mapping_frame_name)
