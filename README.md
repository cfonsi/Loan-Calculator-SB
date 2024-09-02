# Loan-Calculator-SB

## Description
This script contains a function to calculate the projected monthly balance on a loan given the initial loan amount, interest rate, loan term, and monthly payment amount. The remaining balance and interest charged are displayed for each month until the end of the loan term or until the loan is settled.

- **W**: Initial Loan Value (Principal).
- **X**: Annual Interest Rate (as a percentage).
- **Y**: Loan Term (in months).
- **Z**: Monthly Payment Value.


## Usage
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/cfonsi/Loan-Calculator-SB.git
   cd Loan-Calculator-SB
   ```
2. **Run the loan_calculator.py script and enter the values in the command line as prompted:**
   ```bash
   python loan_calculator.py
   ```

## Example
```bash
Please enter the Total Loan Amount: £2000
Please enter the Interest Rate: 6
Please enter the Loan Term in months: 12
Please enter the Monthly Payment Amount: £200
-- Month 1 --
Interest Charged: £10.00
Total Remaining Balance: £1810.00
-- Month 2 --
Interest Charged: £9.05
Total Remaining Balance: £1619.05
-- Month 3 --
Interest Charged: £8.10
Total Remaining Balance: £1427.15
-- Month 4 --
Interest Charged: £7.14
Total Remaining Balance: £1234.28
-- Month 5 --
Interest Charged: £6.17
Total Remaining Balance: £1040.45
-- Month 6 --
Interest Charged: £5.20
Total Remaining Balance: £845.65
-- Month 7 --
Interest Charged: £4.23
Total Remaining Balance: £649.88
-- Month 8 --
Interest Charged: £3.25
Total Remaining Balance: £453.13
-- Month 9 --
Interest Charged: £2.27
Total Remaining Balance: £255.40
-- Month 10 --
Interest Charged: £1.28
Total Remaining Balance: £56.67
-- Month 11 --
Interest Charged: £0.28
Total Remaining Balance: £0.00
Loan Fully Paid in Month 11
```

### Explanation
#### **Loan Details:**
- **Initial Loan Value (W)**: £2000
- **Annual Interest Rate (X)**: 6%
- **Loan Term (Y)**: 12 months
- **Monthly Payment Value (Z)**: £200

#### **Breakdown:**
   - **Annual Interest Rate to a Monthly Rate**:
     - 6% / 12 = 0.5% (0.005 as a decimal).

   - **Month 1**:
     - Interest: £2000 * 0.005 = £10.00
     - Payment: £200.00
     - New Balance: £2000 + £10.00 - £200.00 = £1810.00
  - **Month 2**:
     - Interest: £1810.00 * 0.005 = £9.05
     - Payment: £200.00
     - New Balance: £1810.00 + £9.05 - £200.00 = £1619.05

    ...
  - **Month 10**:
    - Interest Charged: £1.28
    - Payment Made: £200.00
    - Remaining Balance: £56.67
   - **Month 11**:
     - Interest Charged: £0.28
     - Payment Made: £56.95 (to settle the remaining balance and interest)
     - Remaining Balance: £0.00 
    
Loan fully paid off in month 11, before the end of its 12 month term.
  
