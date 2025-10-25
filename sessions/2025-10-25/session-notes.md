# Session Notes - October 25, 2025

## Session Overview
- **Date**: 2025-10-25
- **Duration**: ~60 minutes
- **Format**: Mixed - Practice problem testing + Concept deep dives
- **Main Topics**: Bond yield rankings (verification), Multi-stage dividend discount model, Investment risk types, Options vs Futures
- **Days Until Exam**: 16 days

---

## Practice Problems and Concept Reviews

### Topic 1: Bond Yield Rankings - Practice Verification (D.32)

**Topic**: D.32 Bond and stock valuation - Yield rankings reinforcement

**Purpose**: Test student's retention of yesterday's learning (bond yield rankings)

**Problem Given**: Corporate bond issued 5 years ago, 6% annual coupon, 20-year maturity (15 years remaining), $1,000 par, trading at $920, callable in 3 years at $1,040.

**Question**: Rank yields from LOWEST to HIGHEST: CR, CY, YTM, YTC

**Options**:
- A) CR < CY < YTM < YTC ✓
- B) YTC < YTM < CY < CR
- C) CR < CY < YTC < YTM
- D) CY < CR < YTM < YTC

**Student's Response**: "CR < CY < YTM < YTC" ✓ **CORRECT**

---

**Student's Work Shown**:

**Coupon Rate**: 6% ✓ (correctly identified as fixed)

**Current Yield**:
- Calculation: $60 ÷ $920 = 0.0652 = **6.52%** ✓
- Perfect calculation!

**Bond Status**: Identified as **DISCOUNT bond** ✓
- Price $920 < Par $1,000

**Ranking Applied**: **CR < CY < YTM < YTC** ✓
- Correctly applied discount bond pattern from yesterday's learning!

---

**YTC Calculation Attempt**:

Student attempted: "40/8+60=65, 0.65"
- Trying to approximate YTC
- Got confused on exact method

**Teaching Moment - YTC Approximation Formula**:

After student challenged my initial numbers (correctly!), I searched for proper formula:

**Approximate YTC Formula**:
```
YTC = [Annual Coupon + (Call Price - Current Price) ÷ Years to Call] ÷ [(Call Price + Current Price) ÷ 2]
```

**Applied to our bond**:
- YTC = [$60 + ($1,040 - $920) ÷ 3] ÷ [($1,040 + $920) ÷ 2]
- YTC = [$60 + $40] ÷ $980
- YTC = $100 ÷ $980
- **YTC = 10.2%** ✓

**YTM Approximation**:
- YTM ≈ [$60 + ($1,000 - $920) ÷ 15] ÷ [($1,000 + $920) ÷ 2]
- YTM ≈ [$60 + $5.33] ÷ $960
- **YTM ≈ 6.8%**

**Final Verified Ranking**:
- CR = 6.0% (lowest)
- CY = 6.52%
- YTM = 6.8%
- YTC = 10.2% (highest)

**CR < CY < YTM < YTC** ✓ Student was 100% correct!

---

**Important Teaching Moment - Timeline Clarification**:

**Student's Question**: "Why 3 years for YTC, not 5+3 years?"

**Confusion**: Student thought "issued 5 years ago" + "callable in 3 years" = 8 years

**Clarification Provided**:

**Timeline Visual**:
```
5 years ago              TODAY                3 years           15 years
    |                      |                     |                  |
  Issued              You buy bond          Callable          Maturity
  (20-yr)              at $920              at $1,040         at $1,000
    |                      |                     |                  |
    └──────5 years────────┘                     └────15 years──────┘
    (already passed)                         (remaining to maturity)
                           └────3 years────┘
                          (time until callable)
```

**Key Concept**: All yield calculations start from **TODAY** (when you buy)
- YTC: From TODAY until call (3 years from now)
- YTM: From TODAY until maturity (15 years from now)
- The "5 years ago" is just background info (shows it's a seasoned bond)

**Student Understanding**: ✓ Clarified successfully

---

**Understanding Level**: EXCELLENT
- Correctly applied yesterday's pattern
- Performed calculations accurately
- Challenged instructor when numbers didn't match (critical thinking!)
- Understood timeline clarification

---

### Topic 2: Multi-Stage Dividend Discount Model (D.32)

**Topic**: D.32 Bond and stock valuation - Dividend Discount Model (DDM)

**Problem Given**: ABC Co. will pay dividends of $2, $0, $1 at end of Years 1, 2, 3 respectively. Future dividends (after Year 3) grow at 5% annually. Required return 9%. What is value per share?

**Options**:
- A) 18.60%
- B) 22.88% ✓
- C) 26.25%
- D) 28.86%

**Note**: Answer choices show percentages but should be dollar values (likely formatting error in question)

**Student's Initial Understanding**:
- ✓ Knows Gordon Growth Model: P = D₁ ÷ (r - g)
- ✓ Identified **two stages**: Non-constant dividends (years 1-3), then constant growth
- ✓ Knows denominator is (9% - 5%) = 4%
- ✓ Recognized need to combine $2, $0, $1 with growth portion
- ❓ Confused about HOW to combine the parts

**Student's Quote**: "I remember if you have D1 divided by required return of 9% you get intrinsic value... but here there are three values 2, 0, 1, so there are two stages... I probably think 1.05 divided by (9% - 5%) = 4%... but how does that work together with the 2, 0, 1 I don't know"

---

**Teaching Approach - Building on What Student Knows**:

**Step 1: Value the Non-Constant Dividends (Years 1-3)**

Find **present value** of each dividend:

**Year 1**: $2 ÷ (1.09)¹ = **$1.83**

**Year 2**: $0 ÷ (1.09)² = **$0.00**

**Year 3**: $1 ÷ (1.09)³ = **$0.77**

**Total PV of Years 1-3** = $1.83 + $0 + $0.77 = **$2.60**

---

**Step 2: Value ALL Future Dividends After Year 3**

**KEY INSIGHT**: After Year 3, dividends grow at 5% forever

**Year 4 dividend**:
- Year 3 dividend: $1
- Year 4 dividend: $1 × 1.05 = **$1.05**

**Use Gordon Growth Model at END of Year 3**:

**Value at Year 3** = D₄ ÷ (r - g)
- = $1.05 ÷ (0.09 - 0.05)
- = $1.05 ÷ 0.04
- = **$26.25** ← This is the "terminal value"

**IMPORTANT**: This $26.25 is the value **at the end of Year 3**, not today!

**Bring it back to TODAY** (present value):

**PV of terminal value** = $26.25 ÷ (1.09)³
- = $26.25 ÷ 1.295
- = **$20.27**

---

**Step 3: Add Them Together**

**Total Stock Value TODAY** = PV of Years 1-3 + PV of terminal value

**Stock Value = $2.60 + $20.27 = $22.87** ≈ **$22.88**

---

**The Answer: B) $22.88** (or 22.88% if format is weird)

---

**Visual Timeline Provided**:

```
TODAY          Year 1      Year 2      Year 3      Year 4...∞
  |              |           |           |           |
  |           $2 div      $0 div      $1 div    $1.05 div
  |              |           |           |       (grows 5%)
  |              |           |           |
  └──PV $1.83────┘           |           |
                 └──PV $0────┘           |
                             └──PV $0.77─┘
                                         |
                                    Terminal Value
                                    = $1.05 / 0.04
                                    = $26.25
                                    PV = $20.27

Total = $1.83 + $0 + $0.77 + $20.27 = $22.87
```

---

**The Formula Pattern Taught**:

**Multi-Stage DDM**:

**P₀ = [D₁/(1+r)¹] + [D₂/(1+r)²] + [D₃/(1+r)³] + [P₃/(1+r)³]**

Where **P₃ = D₄/(r-g)** ← This is the Gordon Growth part!

---

**Key Concepts Mastered**:

1. **Two-stage valuation**: Non-constant dividends + constant growth
2. **PV each non-constant dividend** separately
3. **Terminal value** = First constant-growth dividend ÷ (r - g)
4. **Discount terminal value** back to present
5. **Add all PVs** together for total stock value

---

**Understanding Level**: VERY GOOD
- Had right concepts but unclear on execution
- Understood after step-by-step walkthrough
- Grasped the "terminal value at Year 3, then discount back" concept

---

### Topic 3: Investment Risk Types - Physical Gold Liquidity (D.28)

**Topic**: D.28 Types of investment risk - Liquidity risk

**Problem Given**: Which type of risk is an individual most subject to when investing in physical gold?

**Options**:
- A) Liquidity ✓
- B) Commodities
- C) Exchange rate
- D) Constructive receipt

**Student's Response**: "I cannot sell it quickly, so liquidity is going to be a major issue here" ✓ **CORRECT**

**Student's Question**: "I don't know what constructive receipt means"

---

**Correct Answer: A) Liquidity**

**Student's Reasoning** (EXCELLENT):
- ✓ Identified physical gold (can buy at Costco)
- ✓ Recognized difficulty selling quickly
- ✓ Concluded liquidity is major issue

**Teaching - Why Liquidity Risk is Highest for Physical Gold**:

**What is Liquidity Risk?**
- Risk that you **can't sell an asset quickly** at a fair price
- Or you must accept big discount to sell fast

**Physical Gold Problems**:
- ✗ Can't sell instantly (need to find buyer)
- ✗ Verification needed (is it real gold?)
- ✗ Transportation required (physical delivery)
- ✗ Price negotiation (dealers lowball you)
- ✗ Huge bid-ask spread (buy $2,000/oz, sell $1,800/oz)
- ✗ No market hours (can't sell at 2am)

**Student's Costco Example Applied**:
- Buy gold bar at Costco for $2,100
- Emergency happens, need cash NOW
- Pawn shop offers $1,700 (big discount!)
- Or wait days/weeks for better buyer
- **This is liquidity risk!**

---

**Comparison Taught**:

**Physical Gold** (bars, coins):
- **High liquidity risk** ✗
- Takes days to sell
- Big bid-ask spread

**Gold ETF** (like GLD):
- **Low liquidity risk** ✓
- Sell in seconds during market hours
- Tiny spread (pennies)

---

**Why NOT the Other Answers**:

**B) Commodities** ❌
- "Commodities" is NOT a type of risk - it's an **asset class**!
- Like saying "stock risk" or "bond risk" - doesn't make sense
- Risk types: Liquidity, Credit, Market, Interest Rate, etc.

**C) Exchange Rate** ❌
- Exchange rate risk = currency values change
- Applies to foreign investments (Japanese stocks → yen risk)
- Gold is priced in **dollars** in U.S.
- Buy in dollars, sell in dollars
- **No exchange rate risk**

**D) Constructive Receipt** ❌
- **TAX CONCEPT**, not investment risk!
- Income is taxable when you have **right to access it**
- Example: December paycheck ready Dec 31, don't pick up until Jan 2
- Still taxable in December (constructive receipt)
- Completely irrelevant to gold investing!

---

**Asset Liquidity Ranking Taught**:

**Most Liquid** → **Least Liquid**:
1. Cash
2. Money market funds
3. Stocks (large cap)
4. Bonds (Treasury, corporate)
5. Mutual funds
6. Real estate
7. **Physical gold, art, collectibles** ← LEAST liquid

**Physical assets** = **HIGH liquidity risk**

---

**Real-World Example Provided**:

**Scenario**: Own $50,000 in gold bars, need $50,000 cash tomorrow for emergency

**Option 1 - Sell to dealer**:
- Dealer offers $45,000 (10% discount)
- Get cash fast but lose $5,000
- **Liquidity risk cost = $5,000!**

**Option 2 - Find best price**:
- Post online, wait for private buyer
- Get $49,000 (better price)
- Takes 2 weeks - too late!
- **Liquidity risk = can't access money when needed**

**If you had $50K in stock ETF**:
- Sell in 2 seconds
- Get $49,950 (tiny $50 spread)
- Cash in 2 days
- **Low liquidity risk!**

---

**Understanding Level**: EXCELLENT
- Correctly identified answer immediately
- Good intuition about physical asset problems
- Learned tax concept (constructive receipt) vs investment risk distinction

---

### Topic 4: Options vs Futures - Comprehensive Comparison (D.27)

**Topic**: D.27 Investment vehicles - Derivatives (Options and Futures)

**Student's Request**: "Tell me about the difference between options and futures... I remember one is more like a longer version, the other is shorter version, but I don't remember exact details"

**Student's Initial Understanding**:
- ✓ Knows calls vs puts (call = expect up, put = expect down)
- ✓ Understands basic option mechanics
- ❓ Doesn't know what futures contracts are
- ❓ Heard "obligation vs rights" but unclear
- **Focus requested**: Options vs Futures comparison

**Small Correction Made**: Student said "PUDs" - clarified meant "PUTS"

---

**Teaching Approach - The #1 Most Important Difference**:

## OBLIGATION vs. RIGHT

**OPTIONS** = You have a **RIGHT** (not obligation)
- You **CAN** exercise if you want
- You **CAN** let it expire worthless
- You **choose** what to do

**FUTURES** = You have an **OBLIGATION** (must do it!)
- You **MUST** buy or sell at contract expiration
- You **CANNOT** just walk away
- Both parties are **obligated** to execute

---

**Examples Provided**:

### CALL OPTION Example:

**You buy a call option**:
- Strike price: $50
- Stock currently: $45
- Premium paid: $3

**Scenario 1 - Stock goes to $60**:
- ✓ Exercise! Buy at $50, sell at $60
- Profit = $60 - $50 - $3 = $7 per share

**Scenario 2 - Stock drops to $30**:
- ✗ Don't exercise! (Stupid to buy at $50 when market is $30)
- Let option expire worthless
- Loss = $3 premium only (limited loss!)

**Key**: You had a **CHOICE** ← This is option's power!

---

### FUTURES CONTRACT Example:

**You buy futures contract** (agree to buy corn):
- Contract: Buy 5,000 bushels at $5/bushel in 3 months
- Total obligation: $25,000

**Scenario 1 - Corn price goes to $7/bushel**:
- ✓ Great! You buy at $5, market is $7
- Profit = ($7 - $5) × 5,000 = $10,000

**Scenario 2 - Corn price drops to $3/bushel**:
- ✗ **You STILL must buy at $5!** (obligation!)
- Market is $3, you pay $5
- Loss = ($5 - $3) × 5,000 = $10,000 loss!
- **You can't walk away!**

**Key**: You had **NO CHOICE** ← This is futures' risk!

---

**Comprehensive Comparison Table**:

| Feature | **OPTIONS** | **FUTURES** |
|---------|-------------|-------------|
| **Nature** | **RIGHT** to buy/sell | **OBLIGATION** to buy/sell |
| **Upfront Cost** | Pay **premium** | No premium, but **margin** required |
| **Max Loss (buyer)** | **Premium only** (limited) | **Unlimited** |
| **Flexibility** | Can choose not to exercise | **Must** execute contract |
| **Expiration** | Various (weeks to years) | Specific dates (quarterly) |
| **Standardization** | Some customization possible | Highly standardized |
| **Primary Use** | Speculation, hedging | Hedging, price locking |
| **Typical Investor** | Individual investors, smaller | Institutional, businesses, commodities |

---

**The Premium Difference (CRITICAL)**:

### OPTIONS - You Pay a Premium

**Call option example**:
- Pay $3 per share premium **UPFRONT**
- This is your **maximum loss**
- If stock drops, you lose $3, that's it!

### FUTURES - No Premium BUT Margin Required

**Futures contract**:
- **Don't pay premium**
- Must deposit **margin** (security deposit)
- Margin typically 5-15% of contract value
- **But loss can be unlimited!**

**Example**:
- Futures contract: $100,000 value
- Margin required: $10,000 (10%)
- Position moves against you by 20%:
  - Loss = $20,000 (more than margin!)
  - Must add more money or be liquidated

---

**Real-World Use Cases**:

### Who Uses OPTIONS?

**Individual investors**:
- "I think Tesla will go up, let me buy a call"
- Limited risk ($3 premium)
- Can't lose more than premium

**Conservative investors**:
- Protective puts (insurance on stocks)
- Covered calls (income generation)

---

### Who Uses FUTURES?

**Farmers** (hedging):
- Plant corn in April
- Want to lock in price NOW for September harvest
- Sell futures contract at $5/bushel
- Guaranteed price regardless of market
- **This is hedging, not speculation!**

**Airlines** (hedging):
- Need jet fuel for next year
- Worried fuel prices will spike
- Buy futures to lock in price
- **Protects business from price swings**

**Speculators**:
- Day traders betting on commodities
- High leverage (control $100K with $10K margin)
- **Very risky!**

---

**Key Exam Distinctions**:

**OPTIONS**:
- ✓ Limited loss (premium only)
- ✓ More flexibility
- ✓ Good for individual investors
- ✗ Premium can be expensive
- ✗ Time decay (expire worthless if not exercised)

**FUTURES**:
- ✓ No premium upfront
- ✓ Highly liquid markets
- ✓ Perfect for hedging business risk
- ✗ **Unlimited loss potential**
- ✗ Obligation (can't walk away)
- ✗ Margin calls (must add money if position moves)

---

**Memory Tricks Taught**:

**OPTIONS** = "**OP**tional" = You have a choice
- Like having a **coupon** - you CAN use it, but don't have to

**FUTURES** = "**FU**lly committed" = You must do it
- Like signing a **contract** to buy a house - you MUST close

---

**Comprehension Check Questions Given** (for next session):

1. You buy a call option for $5 premium (strike $100). Stock drops to $50. What's your maximum loss?

2. You enter a futures contract to buy oil at $80/barrel. Oil drops to $60. Can you just walk away and lose nothing?

3. Which is riskier for an individual investor - buying a call option or buying a futures contract? Why?

---

**Understanding Level**: EXCELLENT
- Student had good foundation on options (calls/puts)
- Completely new to futures concept
- Grasped the critical "right vs obligation" distinction
- Understood premium vs margin difference
- Appreciated real-world use case examples

---

## Topics Covered Today

| Topic | CFP Code | Confidence | Notes |
|-------|----------|------------|-------|
| Bond Yield Rankings (Review) | D.32 | High | Perfect application of yesterday's pattern |
| YTC Approximation Formula | D.32 | High | Learned proper calculation method |
| Timeline Clarification | D.32 | High | Understood "from today" concept |
| Multi-Stage Dividend Discount Model | D.32 | Medium-High | New concept, needs practice |
| Liquidity Risk - Physical Gold | D.28 | High | Excellent intuition demonstrated |
| **Options vs Futures** | **D.27** | **Medium-High** | **NEW - Comprehensive understanding** |

---

## Key Concepts Mastered

### Bond Yield Rankings - Verification (D.32)
- **Discount bond pattern**: CR < CY < YTM < YTC ✓ retained from yesterday
- **YTC approximation formula**: [Coupon + (Call Price - Current Price)/Years] / [(Call Price + Current Price)/2]
- **Timeline clarity**: All yields calculated from TODAY, not from issuance
- Perfect execution on practice problem

### Multi-Stage Dividend Discount Model (D.32)
- **Step 1**: PV each non-constant dividend separately
- **Step 2**: Calculate terminal value at end of non-constant period (P₃ = D₄/(r-g))
- **Step 3**: Discount terminal value back to present
- **Step 4**: Add all PVs together
- **Formula**: P₀ = Σ[Dₜ/(1+r)ᵗ] + [Pₙ/(1+r)ⁿ]
- Example: $2, $0, $1 then 5% growth → $22.88 value

### Liquidity Risk (D.28)
- **Definition**: Can't sell quickly at fair price
- **Physical gold**: HIGH liquidity risk (days to sell, big spread)
- **Gold ETF**: LOW liquidity risk (seconds to sell, tiny spread)
- **Asset liquidity ranking**: Cash → Stocks → Bonds → Real Estate → Physical assets (least liquid)
- **Not investment risks**: Commodities (asset class), Constructive receipt (tax concept)

### Options vs Futures - Complete Comparison (D.27)

**The #1 Difference - Obligation vs Right**:
- **Options**: RIGHT to buy/sell (can choose not to exercise)
- **Futures**: OBLIGATION to buy/sell (must execute)

**Cost Structure**:
- **Options**: Pay premium upfront (max loss = premium)
- **Futures**: No premium, but margin required (loss can be unlimited)

**Risk Profile**:
- **Options**: Limited downside (premium only)
- **Futures**: Unlimited downside (must honor contract)

**Typical Users**:
- **Options**: Individual investors, speculation, protective strategies
- **Futures**: Businesses hedging, farmers, airlines, speculators

**Memory Tricks**:
- Options = "OPtional" (have choice, like coupon)
- Futures = "FUlly committed" (must do it, like house contract)

**Real-World Examples**:
- Farmer sells corn futures (locks in harvest price)
- Airline buys fuel futures (protects from price spikes)
- Individual buys call option (limited risk speculation)

---

## Progress Assessment

**Topics Reinforced**:
- D.32 Bond valuation (yield rankings, YTC calculation)
- D.28 Investment risk (liquidity risk identification)

**New Topics Added**:
- D.32 Multi-stage dividend discount model (DDM)
- D.27 Options vs Futures (derivatives comparison)

**Strengths Observed**:
- Excellent retention from previous session (bond yield rankings)
- Strong critical thinking (challenged instructor's numbers - was right!)
- Good intuition (physical gold liquidity)
- Quick learner (grasped futures obligation concept immediately)
- Asked clarifying questions (timeline for YTC)

**Areas for Continued Practice**:
- Multi-stage DDM calculations (needs more practice problems)
- Options strategies (covered calls, protective puts)
- Futures margin and leverage calculations

---

## Session Statistics

**Session Duration**: ~60 minutes
**Topics Covered**: 4 major topics (bond yields review, DDM, liquidity risk, options vs futures)
**Format**: Mixed (practice testing + new concept teaching)
**Performance**: Excellent - strong retention, good intuition, quick learning

**Days Until Exam**: 16 days

---

## Notes

**Day 6 of Study Plan - October 25, 2025**

Mixed session combining practice problem verification (testing yesterday's learning) with new concept introduction. Student demonstrated excellent retention of bond yield rankings and strong critical thinking by challenging instructor calculations.

**Major Learning Achievements**:
- Verified bond yield ranking pattern retention (discount bonds)
- Learned proper YTC approximation formula
- Mastered multi-stage dividend discount model
- Identified liquidity risk correctly with good reasoning
- **Comprehensively understood Options vs Futures distinction**

**Critical Thinking Demonstrated**:
- Challenged instructor on YTC calculation discrepancy (7.8% vs 10.2%)
- Asked excellent clarifying question about timeline (5 years ago + 3 years)
- Correctly identified liquidity as main risk for physical gold

**Key Pattern Reinforced**:
- All yield calculations start from TODAY (purchase date)
- Terminal value in DDM must be discounted back to present
- Physical assets have highest liquidity risk

**Ready for**: Continue D.27 (investment vehicles - stocks, bonds, mutual funds, REITs) or move to D.30-D.31 (quantitative concepts)

**Investment Planning Progress**: 7/9 topics (78%) - nearing completion!

---

**Session Status**: COMPLETE - Ready to save

---

# Session Continuation - October 25, 2025 (Part 2)

## Session Overview - Part 2
- **Date**: 2025-10-25
- **Duration**: ~45 minutes
- **Format**: Practice problem testing - mixed topics
- **Main Topics**: Portfolio immunization, Capital loss carryover, Modified duration, CAPM, Gordon Growth Model with retention ratio
- **Days Until Exam**: 16 days

---

## Practice Problems - Session Continuation

### Topic 5: Portfolio Immunization (D.32)

**Topic**: D.32 Bond and stock valuation - Portfolio immunization strategy

**Problem Given**: Portfolio immunization attempts to balance which two of the following components of interest rate risk?
- Price risk and credit risk
- Price risk and reinvestment risk ✓
- Reinvestment risk and credit risk
- Default risk and price risk

**Student's Initial Understanding**:
- ❓ Not familiar with "portfolio immunization" term
- Initial thought: "Sounds like building a good portfolio, removing unsystematic risk"
- Confused immunization with diversification

---

**Teaching Approach - What is Portfolio Immunization?**

**Portfolio immunization** is a bond strategy that protects against **interest rate risk** when you have a future liability to pay (e.g., pension payment in 10 years).

**The Key Insight**: When interest rates change, two opposite things happen:

1. **Price Risk**: Rates UP → Bond prices DOWN (you lose on bond value)
2. **Reinvestment Risk**: Rates UP → Reinvest coupons at HIGHER rates (you gain on reinvestment)

**These two risks move in OPPOSITE directions!**

Immunization balances them so they **cancel each other out**.

---

**Concrete Example Provided**:

**Scenario**: Pension fund manager needs to pay $100,000 in exactly 5 years

**Strategy**: Buy 5-year bond, 6% coupon, $100,000 face value

**What happens if rates RISE to 8% right after purchase?**

**Loss from Price Risk**:
- Bond market value drops to ~$92,000 (rates up = price down)
- Loss: **$8,000**

**Gain from Reinvestment Risk**:
- Year 1-4 coupons: $6,000/year
- Now reinvest at 8% instead of 6%
- Extra gain from higher reinvestment: **~$8,000**

**The two cancel out!** Still end up with $100,000 to pay retiree.

---

**The Seesaw Analogy**:
- Rates go UP → Bond prices FALL (bad) BUT reinvestment income RISES (good)
- Rates go DOWN → Bond prices RISE (good) BUT reinvestment income FALLS (bad)

When perfectly immunized, these effects offset each other.

**Key to immunization**: Match bond's **duration** to time horizon (5 years)

---

**Answer: Price risk and reinvestment risk** ✓

---

**Understanding Level**: GOOD
- Initially confused with diversification
- Quickly grasped the offsetting risk concept
- Understood real-world application (pension fund example)

---

### Topic 6: Capital Loss Carryover and Municipal Bond Taxation (E.40, E.36)

**Topic**: E.40 Tax reduction techniques, E.36 Income taxation fundamentals

**Problem Given**: Investor with $100,000 short-term capital loss carryover invests equal amounts in each position. Which has GREATEST reduction to capital loss carryover?

**Options**:
- A) Municipal bonds 5% coupon, home state, bought at 5% discount, held to par
- B) Municipal bonds 5% coupon, home state, bought at 5% discount, sold at premium ✓
- C) Commercial non-qualified deferred fixed annuity, 5% bonus, 5% guaranteed floor
- D) Domestic zero-coupon treasuries, 5% discount, held to maturity, 5% imputed yield

---

**Student's Initial Analysis** (EXCELLENT):

Student's reasoning:
- "They're asking who gives max return, right?"
- "Short-term capital loss can offset any type of capital gain"
- "B definitely gives you more"
- "Annuity gives income tax, not capital gain tax" ✓

**Student understanding**: ✓ Correct reasoning!

---

**Teaching - Tax Treatment of Each Option**:

**Option A - Muni bond discount, held to par**:
- 5% discount = **ordinary income** (not capital gain)
- Tax rule: "Market discount" on bonds = ordinary income
- Zero capital gain → Can't offset loss carryover

**Option B - Muni bond discount, sold at premium** ✓:
- Gain from selling at premium = **CAPITAL GAIN** (taxable!)
- Note: Muni bond INTEREST is tax-free, but CAPITAL GAINS are taxable
- Creates biggest capital gain → Reduces loss carryover most

**Option C - Annuity**:
- Student correctly identified: **ordinary income**, not capital gain ✓
- Can't offset capital loss

**Option D - Zero-coupon treasury, held to maturity**:
- Original Issue Discount (OID) = **ordinary income**
- Taxed EVERY YEAR as "phantom income" (even without cash!)
- When held to maturity: zero capital gain
- Can't offset loss carryover

---

**Critical Tax Learning - Municipal Bonds Have TWO Types of Income**:

**1. INTEREST income** (coupon payments):
- Federal tax: **EXEMPT** (tax-free)
- State tax: **EXEMPT if home state resident**
- Triple-tax-free if local muni

**2. CAPITAL GAINS** (when sold at profit):
- Federal tax: **TAXABLE**
- State tax: **TAXABLE**
- No exemption!

---

**Student's Initial MISCONCEPTION** (corrected):

**Student said**: "Federal bonds pay federal tax not state tax, state muni bonds pay state tax not federal tax, but if local resident you pay no tax"

**CORRECTION PROVIDED**:

**Municipal Bonds**:
- INTEREST: Federal exempt, state exempt if home state
- CAPITAL GAINS: Fully taxable (federal AND state)

**Federal Bonds (Treasuries)**:
- INTEREST: Federal taxable, state exempt
- CAPITAL GAINS: Fully taxable (both levels)

---

**The Key Insight**: Municipal bond in home state = tax-free interest, BUT when sold at premium, that capital gain IS taxable - which is exactly what's needed to offset capital loss carryover!

---

**Answer: B** ✓

---

**Understanding Level**: VERY GOOD
- Student's initial reasoning was excellent ✓
- Learned critical distinction: Interest vs capital gains on munis
- Corrected misconception about muni bond taxation
- Understood all options create ordinary income except B

---

### Topic 7: Modified Duration and Bond Price Sensitivity (D.32)

**Topic**: D.32 Bond and stock valuation - Duration as price sensitivity tool

**Problem Given**: Bond has duration of 10 years, market rates 8%. By approximately how much would bond price decrease if rates increase to 10%?
- A) 10.00%
- B) 18.50% ✓
- C) 20.00%
- D) 21.60%

---

**Student's Initial Understanding**:
- ✓ Knows duration intuition: "How long to get all money back"
- ❓ "For things like this I have no idea how to even start to calculate"
- Lacks practical application formula

---

**Instructor's First Attempt** (WRONG - Student Called It Out!):

Instructor provided simple formula:
```
% Price Change ≈ -Duration × Change in Yield
= -10 × 0.02 = -20%
```

Instructor said answer was **20.00%** (Option C)

**Student's Response**: "I was told the correct answer is 18.50%, can you do some research and don't bullshit me"

✓ **Student was RIGHT to call this out!**

---

**After Online Research - CORRECT Method**:

**The Issue**: There are TWO types of duration:

1. **Macaulay Duration** - measured in YEARS (what question gave: 10 years)
2. **Modified Duration** - used for price change calculations

**Step 1: Convert to Modified Duration**
```
Modified Duration = Macaulay Duration / (1 + Current Yield)
Modified Duration = 10 / (1 + 0.08)
Modified Duration = 10 / 1.08
Modified Duration = 9.26
```

**Step 2: Calculate Price Change**
```
% Price Change = -Modified Duration × Change in Yield
% Price Change = -9.26 × 0.02
% Price Change = -0.1852 = -18.52%
```

**Answer: 18.50% (Option B)** ✓

---

**What Instructor Did Wrong**: Used Macaulay Duration (10) directly in price change formula, giving rough approximation of 20%. CORRECT method requires converting to Modified Duration first.

**Key Takeaway for CFP Exam**: When given duration in years, convert to Modified Duration by dividing by (1 + current yield) before calculating price changes!

---

**Formula to Memorize**:
```
Modified Duration = Macaulay Duration / (1 + y)

% Price Change = -Modified Duration × Δy
```

---

**Understanding Level**: EXCELLENT
- Student correctly challenged wrong answer
- Demanded proper research-based solution ✓
- Learned critical distinction: Macaulay vs Modified Duration
- Understood conversion process

---

### Topic 8: CAPM Formula (D.30)

**Topic**: D.30 Quantitative investment concepts - Capital Asset Pricing Model

**Problem Given**: Stock has beta 1.20, risk-free rate 1%, risk premium 7%. What is required rate of return?
- A) 8.2%
- B) 8.4%
- C) 9.4% ✓
- D) 9.6%

---

**Student's Initial Attempt**:

Student's thinking: "There is x (required return), need to use that minus 1% risk-free, times beta 1.2, plus risk-free premium 7%. But then it equals to what? I don't know how to solve that x."

**Issue**: Student thought they needed to solve an equation for x

---

**Teaching - CAPM Formula Structure**:

**CAPM Formula** (Capital Asset Pricing Model):
```
Required Return = Risk-free Rate + Beta × Market Risk Premium
```

**You DON'T solve for x!** The formula directly GIVES you required return.

---

**Given Information**:
- Risk-free rate = 1%
- Beta = 1.20
- Market risk premium = 7%

**Plug into Formula**:
```
Required Return = 1% + (1.20 × 7%)
Required Return = 1% + 8.4%
Required Return = 9.4%
```

**Answer: 9.4% (Option C)** ✓

---

**What This Means**:
- Start with risk-free rate (1%) - what you'd get from T-bills
- Add risk premium for THIS stock = Beta × Market Risk Premium
- Beta of 1.20 = 20% MORE volatile than market
- Should earn 1.20 times market's 7% premium = 8.4% extra
- Total required return = 1% + 8.4% = 9.4%

---

**Understanding Level**: GOOD
- Initially confused about equation structure
- Quickly understood after formula clarification
- Grasped beta's role (volatility multiplier)
- Can apply formula correctly

---

### Topic 9: Gordon Growth Model with Retention Ratio (D.32)

**Topic**: D.32 Bond and stock valuation - Dividend discount model with growth

**Problem Given**: Company MSR - ROE 12.5%, retention ratio 50%, required return 12%, recently paid dividend $3.50. What is intrinsic value?
- A) 55.52%
- B) 56%
- C) 60.87%
- D) 64.70% ✓

*(Note: Answer choices show % but should be dollars)*

---

**Student's Initial Understanding**:
- ✓ Remembers Gordon Growth Model from earlier today
- ❓ "I have no idea, especially the retention ratio, what's that even"
- Needs to learn retention ratio concept

---

**Teaching - Retention Ratio**:

**Retention Ratio** = % of earnings company KEEPS (retains) instead of paying as dividends

- Retention ratio = 50% → company keeps half, pays out half
- **Payout Ratio** = 1 - Retention Ratio = 50%

**Why It Matters**: Retained money gets reinvested to grow the business!

**Growth Rate Formula**:
```
Growth Rate (g) = ROE × Retention Ratio
```

**Intuition**: If company earns 12.5% ROE and reinvests 50% of earnings:
```
g = 12.5% × 50% = 6.25%
```

---

**Step-by-Step Solution**:

**Step 1: Calculate Growth Rate**
```
g = ROE × Retention Ratio
g = 12.5% × 0.50 = 6.25%
```

**Step 2: Calculate Next Year's Dividend (D₁)**
```
D₁ = D₀ × (1 + g)
D₁ = $3.50 × 1.0625 = $3.71875
```

**Step 3: Use Gordon Growth Model**
```
Intrinsic Value = D₁ / (r - g)
Intrinsic Value = $3.71875 / (0.12 - 0.0625)
Intrinsic Value = $3.71875 / 0.0575
Intrinsic Value = $64.67
```

**Answer: $64.70 (Option D)** ✓

---

**Key Formulas Learned**:

**Growth Rate**:
```
g = ROE × Retention Ratio
```

**Gordon Growth Model**:
```
P₀ = D₁ / (r - g)
```

**Where**:
- D₁ = Next year's dividend = D₀ × (1 + g)
- r = Required return
- g = Growth rate

---

**Understanding Level**: GOOD
- New concept (retention ratio) learned successfully
- Connected to Gordon Growth Model from earlier
- Understood growth calculation logic
- Can apply formula correctly

---

## Topics Covered - Session Part 2

| Topic | CFP Code | Confidence | Notes |
|-------|----------|------------|-------|
| Portfolio Immunization | D.32 | Medium-High | New concept - price risk vs reinvestment risk |
| Capital Loss Carryover | E.40 | High | Excellent reasoning, learned muni tax rules |
| Municipal Bond Taxation | E.36 | High | Interest tax-free, capital gains taxable |
| Modified Duration | D.32 | High | Critical distinction from Macaulay duration |
| CAPM Formula | D.30 | High | Formula structure mastered |
| Gordon Growth with Retention | D.32 | Medium-High | New concept - retention ratio |

---

## Key Concepts Mastered - Part 2

### Portfolio Immunization (D.32)
- Balances **price risk** and **reinvestment risk**
- When rates rise: prices fall BUT reinvestment income rises
- When rates fall: prices rise BUT reinvestment income falls
- Match bond duration to liability time horizon
- Offsetting risks protect against rate changes

### Capital Loss and Municipal Bond Taxation (E.36, E.40)
- Short-term capital loss can offset ANY capital gain
- Municipal bonds have TWO income types:
  1. **Interest**: Tax-free (federal and home state)
  2. **Capital gains**: FULLY TAXABLE
- Market discount on bonds = ordinary income (not capital gain)
- OID on zero-coupon bonds = ordinary income taxed annually
- Only Option B created capital gain to offset loss

### Modified Duration (D.32)
- **Macaulay Duration**: Time-weighted measure (in years)
- **Modified Duration**: Price sensitivity measure
- **Conversion**: Modified = Macaulay / (1 + yield)
- **Price change formula**: % Change = -Modified Duration × Δyield
- Example: Duration 10, yield 8% → Modified = 9.26
- 2% rate increase → -18.5% price change

### CAPM - Capital Asset Pricing Model (D.30)
- **Formula**: Required Return = Risk-free Rate + Beta × Market Risk Premium
- Beta measures stock volatility vs market
- Beta > 1: More volatile than market
- Beta < 1: Less volatile than market
- Beta = 1: Same as market
- Example: Beta 1.20 means 20% more volatile

### Gordon Growth Model with Retention Ratio (D.32)
- **Retention Ratio**: % of earnings kept (not paid as dividends)
- **Payout Ratio**: 1 - Retention Ratio
- **Growth Rate**: g = ROE × Retention Ratio
- **Gordon Model**: P₀ = D₁ / (r - g)
- Higher retention = higher growth but lower current dividends
- Trade-off between current income and future growth

---

## Progress Assessment - Part 2

**New Topics Added**:
- D.30 Quantitative investment concepts (CAPM) ← NEW!
- E.36 Income tax fundamentals (muni bond taxation)
- E.40 Tax reduction techniques (capital loss carryover)

**Topics Reinforced**:
- D.32 Bond/stock valuation (immunization, duration, Gordon Growth)

**Strengths Observed**:
- Excellent critical thinking (called out wrong duration answer)
- Strong initial reasoning (capital loss problem)
- Demanded accuracy and research-based answers ✓
- Quick learning on new concepts (retention ratio)

**Areas for Continued Practice**:
- Modified duration calculations (now mastered)
- CAPM applications with different betas
- Multi-stage DDM vs Gordon Growth

---

## Session Statistics - Part 2

**Session Duration**: ~45 minutes
**Topics Covered**: 5 major topics across 3 domains (D, E)
**Format**: Practice problem testing
**Performance**: Excellent - challenged incorrect answers, demanded precision

**Days Until Exam**: 16 days

---

## Notes - Session Part 2

**Critical Achievement**: Student demanded accuracy and called out instructor's wrong answer on modified duration - then got proper research-based solution. This demonstrates excellent critical thinking and willingness to challenge authority when numbers don't make sense.

**Major Learning**:
- Portfolio immunization concept (offsetting risks)
- Municipal bond taxation (interest vs capital gains)
- Modified vs Macaulay duration (critical CFP exam distinction)
- CAPM formula application
- Retention ratio and growth rate relationship

**Investment Planning Domain**: Made progress on D.30 (quantitative concepts) - now 8/9 topics (89%)!

**Tax Planning Domain**: Added E.36 and E.40 coverage

**Ready for**: Complete Investment Planning (D.31 only remaining), or move to high-priority gaps (E.38 Business Taxation, General Principles domain)
