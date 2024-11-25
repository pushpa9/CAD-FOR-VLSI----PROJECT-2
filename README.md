# PROJECT 2 : 4x4 Systolic Array Design

### Pushpa Chaudhary - EE21B109, Fardeen Razif - EE21B046

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

1. **Mac_systolic_array bsv design **: Pushpa  
2. **Cocotb testbench (`test_mac.py`) and `model_mac.py`**: Pushpa
3. **`model_mac.py`**: Fardeen
4. **General debugging**: Both  
5. **Readme**: Pushpa
