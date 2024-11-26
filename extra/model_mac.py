import cocotb
from cocotb_coverage.coverage import *
import numpy as np

# Define coverage for inputs
systolic_coverage = coverage_section(
    CoverPoint('top.EN_get_A', vname='EN_get_A', bins=list(range(0, 2))),
    CoverPoint('top.EN_get_B', vname='EN_get_B', bins=list(range(0, 2))),
    CoverPoint('top.EN_get_C', vname='EN_get_C', bins=list(range(0, 2))),
    CoverPoint('top.EN_s1_or_s2', vname='EN_s1_or_s2', bins=list(range(0, 2))),
    CoverPoint('top.get_A_x', vname='get_A_x', bins=list(range(-128, 128))),  # int8
    CoverPoint('top.get_B_y', vname='get_B_y', bins=list(range(-128, 128))),
    CoverPoint('top.get_C_z', vname='get_C_z', bins=list(range(-2147483648, 2147483648))),  # int32
    CoverPoint('top.s1_or_s2_tcs', vname='s1_or_s2_tcs', bins=list(range(0, 2)))
)

@systolic_coverage
def model_systolic_array(EN_get_A: int, EN_get_B: int, EN_get_C: int, EN_s1_or_s2: int, get_A_x: list, get_B_y: list, get_C_z: list, s1_or_s2_tcs: int) -> list:
    """
    Function to model 4x4 systolic array matrix multiplication.
    Inputs:
    - EN_get_A, EN_get_B, EN_get_C, EN_s1_or_s2: Control signals (1 to enable)
    - get_A_x: 4x4 list of A matrix values (row-major order)
    - get_B_y: 4x4 list of B matrix values (row-major order)
    - get_C_z: 4x4 list of C matrix values (row-major order)
    - s1_or_s2_tcs: 0 (int8) or 1 (bfloat16)
    
    Output:
    - 4x4 list (row-major order) of systolic array computation result
    """
    
	 if EN_get_A and EN_get_B and EN_get_C and EN_s1_or_s2:
		 # Convert inputs into 4x4 matrices
		 A = np.array(get_A_x, dtype=np.float32 if s1_or_s2_tcs else np.int32).reshape((4, 4))
		 B = np.array(get_B_y, dtype=np.float32 if s1_or_s2_tcs else np.int32).reshape((4, 4))
		 C = np.array(get_C_z, dtype=np.float32 if s1_or_s2_tcs else np.int32).reshape((4, 4))

		 # Compute matrix multiplication and add C (element-wise)
		 result = np.matmul(A, B) + C

    if EN_get_A and EN_get_B and EN_get_C and not EN_s1_or_s2_tcs:
        # For int8, constrain the results to 32-bit integers
        result = result.astype(np.int32) & 0xFFFFFFFF
        result[result > 0x7FFFFFFF] -= 0x100000000  # Convert to signed int32 if needed

    # Return as flattened list (row-major order)
    return result.flatten().tolist()

