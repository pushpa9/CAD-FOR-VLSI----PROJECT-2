# PROJECT 2 : 4x4 Systolic Array Design

### Pushpa Chaudhary - EE21B109, Fardeen Razif - EE21B046

## Design Details

### 1. **InnerMac Module**
- Implements the core functionality of a single MAC (Multiply-Accumulate) operation.
- Reuses the MAC logic from Project 1.

### 2. **OuterMac Module**
- Acts as a wrapper for the `InnerMac` module.
- Stores inputs (`A`, `B`, `C`, and `S`) in registers before passing them to the `InnerMac`.
- Additionally, it returns the values of `A` and `B` alongside the results.

### 3. **Mac Module**
- Constructs a **4x4 systolic array** from a 4x4 grid of `OuterMac` modules.
- At every clock cycle:
  - Propagates `B` and the results of `OuterMac` through the rows.
  - Propagates `A` through the columns.
- Outputs a 1x4 vector of results from the last row of `MAC` operations.

## Verification Methodology

There is a `test_mac.py` file which implements a cocotb testbench and verifies the random inputs using `model_mac.py`, which gives the expected output. It is also used in coverage.  
Inputs are given and output is read as shown in the PDF.  

### Note:
- `S = 1` -> `int32`
- `S = 0` -> `bfp16`

## How to Run

* Download the `.zip` file. It would have a `mac_systolic_array` folder. 
* Enter into this directory.
* Enter `make clean` command to wipe off any previous compilations and then `make generate_verilog` command to compile and generate a Verilog file for the BSV design.
* `Mac_verif` folder inside the directory has `test_mac.py` as the cocotb testbench.
  * `test_mac.py` verifies the design for any random test case.
* Enter desired/random input and enter `make simulate` command to run this `.py` testbench.
  * It will verify the results using output generated from `model_mac.py` file and will fail if any assertions fail.
  * Make sure to change `s` accordingly (`s = 1` for `int32`, `s = 0` for `bfloat16`).

### Status
1. **int32**:
   * Code - completed
   * Verification - not completed
2. **bfloat16**:
   * Code - completed
   * Verification - not completed
  
### Separate Contributions

1. **Mac_systolic_array bsv design**: Pushpa  
2. **Cocotb testbench (`test_mac.py`) and `model_mac.py`**: Pushpa
3. **`model_mac.py`**: Fardeen
4. **General debugging**: Both  
5. **Readme**: Pushpa
