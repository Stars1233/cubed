__all__ = []

__array_api_version__ = "2023.12"

from .inspection import __array_namespace_info__

__all__ += ["__array_api_version__", "__array_namespace_info__"]

from .array_object import Array

__all__ += ["Array"]

from .constants import e, inf, nan, newaxis, pi

__all__ += ["e", "inf", "nan", "newaxis", "pi"]

from .creation_functions import (
    arange,
    asarray,
    empty,
    empty_like,
    eye,
    full,
    full_like,
    linspace,
    meshgrid,
    ones,
    ones_like,
    tril,
    triu,
    zeros,
    zeros_like,
)

__all__ += [
    "arange",
    "asarray",
    "empty",
    "empty_like",
    "eye",
    "full",
    "full_like",
    "linspace",
    "meshgrid",
    "ones",
    "ones_like",
    "tril",
    "triu",
    "zeros",
    "zeros_like",
]

from .data_type_functions import astype, can_cast, finfo, iinfo, isdtype, result_type

__all__ += ["astype", "can_cast", "finfo", "iinfo", "isdtype", "result_type"]

from .dtypes import (
    bool,
    complex64,
    complex128,
    float32,
    float64,
    int8,
    int16,
    int32,
    int64,
    uint8,
    uint16,
    uint32,
    uint64,
)

__all__ += [
    "bool",
    "complex64",
    "complex128",
    "float32",
    "float64",
    "int8",
    "int16",
    "int32",
    "int64",
    "uint8",
    "uint16",
    "uint32",
    "uint64",
]

from .elementwise_functions import (
    abs,
    acos,
    acosh,
    add,
    asin,
    asinh,
    atan,
    atan2,
    atanh,
    bitwise_and,
    bitwise_invert,
    bitwise_left_shift,
    bitwise_or,
    bitwise_right_shift,
    bitwise_xor,
    ceil,
    clip,
    conj,
    copysign,
    cos,
    cosh,
    divide,
    equal,
    exp,
    expm1,
    floor,
    floor_divide,
    greater,
    greater_equal,
    hypot,
    imag,
    isfinite,
    isinf,
    isnan,
    less,
    less_equal,
    log,
    log1p,
    log2,
    log10,
    logaddexp,
    logical_and,
    logical_not,
    logical_or,
    logical_xor,
    maximum,
    minimum,
    multiply,
    negative,
    nextafter,
    not_equal,
    positive,
    pow,
    real,
    reciprocal,
    remainder,
    round,
    sign,
    signbit,
    sin,
    sinh,
    sqrt,
    square,
    subtract,
    tan,
    tanh,
    trunc,
)

__all__ += [
    "abs",
    "acos",
    "acosh",
    "add",
    "asin",
    "asinh",
    "atan",
    "atan2",
    "atanh",
    "bitwise_and",
    "bitwise_invert",
    "bitwise_left_shift",
    "bitwise_or",
    "bitwise_right_shift",
    "bitwise_xor",
    "ceil",
    "clip",
    "conj",
    "copysign",
    "cos",
    "cosh",
    "divide",
    "equal",
    "exp",
    "expm1",
    "floor",
    "floor_divide",
    "greater",
    "greater_equal",
    "hypot",
    "imag",
    "isfinite",
    "isinf",
    "isnan",
    "less",
    "less_equal",
    "log",
    "log1p",
    "log2",
    "log10",
    "logaddexp",
    "logical_and",
    "logical_not",
    "logical_or",
    "logical_xor",
    "maximum",
    "minimum",
    "multiply",
    "nextafter",
    "negative",
    "not_equal",
    "positive",
    "pow",
    "real",
    "reciprocal",
    "remainder",
    "round",
    "sign",
    "signbit",
    "sin",
    "sinh",
    "sqrt",
    "square",
    "subtract",
    "tan",
    "tanh",
    "trunc",
]

from .indexing_functions import take

__all__ += ["take"]

from .linear_algebra_functions import matmul, matrix_transpose, tensordot, vecdot

__all__ += ["matmul", "matrix_transpose", "tensordot", "vecdot"]

from .manipulation_functions import (
    broadcast_arrays,
    broadcast_to,
    concat,
    expand_dims,
    flip,
    moveaxis,
    permute_dims,
    repeat,
    reshape,
    roll,
    squeeze,
    stack,
    tile,
    unstack,
)

__all__ += [
    "broadcast_arrays",
    "broadcast_to",
    "concat",
    "expand_dims",
    "flip",
    "moveaxis",
    "permute_dims",
    "repeat",
    "reshape",
    "roll",
    "squeeze",
    "stack",
    "tile",
    "unstack",
]

from .searching_functions import argmax, argmin, count_nonzero, searchsorted, where

__all__ += ["argmax", "argmin", "count_nonzero", "searchsorted", "where"]

from .statistical_functions import cumulative_sum, max, mean, min, prod, std, sum, var

__all__ += ["cumulative_sum", "max", "mean", "min", "prod", "std", "sum", "var"]

from .utility_functions import all, any

__all__ += ["all", "any"]
