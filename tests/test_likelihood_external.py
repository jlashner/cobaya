"""
Tests the facility for importing external likelihoods.

It tests all possible input methods: callable and string
(direct evaluation and ``import_module``).

In each case, it tests the correctness of the values generated, and of the updated info.

The test likelihood is a gaussian half-ring, combined with a gaussian in one of the tests.

For manual testing, and observing/plotting the density, pass ``manual=True`` to
``body of test``.
"""

# Global
from __future__ import division

# Local
from cobaya.conventions import _likelihood
from common_external import info_string, info_callable, info_mixed, info_import
from common_external import info_derived, body_of_test


def test_likelihood_external_string(tmpdir):
    body_of_test(info_string, _likelihood, tmpdir)


def test_likelihood_external_callable(tmpdir):
    body_of_test(info_callable, _likelihood, tmpdir)


def test_likelihood_external_mixed(tmpdir):
    body_of_test(info_mixed, _likelihood, tmpdir)


def test_likelihood_external_import(tmpdir):
    body_of_test(info_import, _likelihood, tmpdir)


def test_likelihood_external_derived(tmpdir):
    body_of_test(info_derived, _likelihood, tmpdir, derived=True)