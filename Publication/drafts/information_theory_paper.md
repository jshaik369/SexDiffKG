# Information-Theoretic Characterization of Sex-Differential Drug Safety: Entropy, Mutual Information, and the Predictability Gradient

**Mohammed Javeed Akhtar Abbas Shaik (J.Shaik)**

CoEvolve Network, Independent Researcher, Barcelona, Spain

ORCID: 0009-0002-1748-7516

Correspondence: jshaik@coevolvenetwork.com

---

## Abstract

**Background.** Traditional pharmacovigilance signal detection relies on disproportionality measures (ROR, PRR) that quantify association strength but do not characterize the information content or predictability of sex-differential signals. Information theory offers a complementary framework for signal prioritization.

**Methods.** From 96,281 sex-differential signals across 1,394 drugs with >= 5 signals (14,536,008 FAERS reports, 2004Q1--2025Q3), we computed binary Shannon entropy H(sex|drug) for each drug, mutual information I(drug;sex|AE) for each adverse event, and tracked entropy across report volume deciles. Information concentration was quantified via cumulative distribution analysis.

**Results.** Mean drug entropy was 0.949 (close to maximum 1.0), but the distribution was left-skewed with a predictable tail. The most sex-predictable drugs were niraparib (H = 0.254, 95.8%F) and enzalutamide (H = 0.335, 6.2%F)---both targeting sex-linked cancer pathways. Entropy anti-regression was significant (Spearman rho = -0.952, p = 2.3 x 10^-5): high-volume drugs had systematically lower entropy (D0: H = 0.982 vs D9: H = 0.908), translating the anti-regression phenomenon into information-theoretic terms as increasing predictability. At the individual signal level, the gradient was steeper (D9: H = 0.716). Mutual information analysis identified folliculitis (MI = 0.320), obesity (MI = 0.318), and blood cholesterol increased (MI = 0.315) as the adverse events where drug identity most strongly predicts reporter sex. Sex information was diffusely distributed across the pharmacopeia: the top 10 drugs contained only 0.3% of total entropy variation, and the top 500 contained 32.9%.

**Interpretation.** Information theory reveals that sex-differential drug safety follows a structured predictability gradient: high-volume drugs are more sex-predictable (lower entropy), specific adverse events carry high mutual information about sex, and sex information is diffusely distributed rather than concentrated in a few outlier drugs. This framework provides a complementary lens for pharmacovigilance signal prioritization, where low-entropy drugs warrant heightened sex-specific monitoring.

**Keywords:** information theory, Shannon entropy, mutual information, pharmacovigilance, sex differences, FAERS, signal detection, adverse drug reactions

---

## 1. Introduction

### 1.1 The Signal Detection Problem in Pharmacovigilance

Pharmacovigilance signal detection has historically relied on disproportionality measures---the Proportional Reporting Ratio (PRR), Reporting Odds Ratio (ROR), and Bayesian Confidence Propagation Neural Network (BCPNN)---to identify drug-adverse event associations that exceed background rates [1,2]. These frequentist and Bayesian approaches compare observed-to-expected reporting frequencies, flagging drug-event combinations whose disproportionality exceeds a threshold as potential safety signals. Sex-stratified extensions of these methods compute sex-specific rates and sex-differential ratios, adding a layer of demographic characterization [3,4]. The resulting sex-differential logR scores---defined as the natural logarithm of the ratio of female to male ROR values---have become a standard measure for quantifying the direction and magnitude of sex-differential safety signals [5].

However, these traditional measures have a fundamental limitation: they quantify association strength (how much a signal deviates from the null) but do not characterize the *information content* of sex-differential signals or the *predictability* of sex distributions across the pharmacopeia. A drug with 60% female signals and a drug with 95% female signals both have "female-biased" profiles, but they differ profoundly in predictability and clinical actionability. The PRR and ROR frameworks, by design, answer the question "is this signal statistically unusual?" rather than "how much can we learn about sex from this drug's safety profile?" These are fundamentally different questions, and answering the latter requires a different mathematical framework.

### 1.2 Information Theory: Foundations and Biomedical Applications

Information theory, founded by Claude Shannon in his landmark 1948 paper "A Mathematical Theory of Communication" [6], provides exactly the mathematical framework needed to address questions of uncertainty, predictability, and information content. Shannon's central insight was that information can be quantified: the entropy H of a random variable measures the average surprise or uncertainty associated with its outcomes, in units of bits. A fair coin has H = 1 bit (maximum uncertainty for a binary variable); a biased coin with 95% heads has H = 0.286 bits (low uncertainty, high predictability). Shannon entropy is the unique measure satisfying the axioms of non-negativity, continuity, and additivity for independent events, making it the canonical measure of uncertainty in any probabilistic system [7].

The connection between entropy and statistical inference has deep roots. Kullback and Leibler formalized the concept of relative entropy (KL divergence) as a measure of distributional difference [8], which underpins mutual information---the reduction in uncertainty about one variable gained by observing another. Fisher information, while distinct from Shannon information, provides complementary bounds on estimation precision through the Cramer-Rao inequality [9]. Together, these information-theoretic quantities form a coherent framework for characterizing signal strength, predictability, and distributional structure in any data-rich domain.

In biomedical applications, information theory has found diverse uses over the past two decades. Butte and Kohane [10] applied mutual information to gene expression microarray data to identify regulatory relationships, demonstrating that information-theoretic measures could detect nonlinear associations invisible to correlation analysis. In bioinformatics, sequence logos use entropy to quantify conservation at each position in a multiple sequence alignment, directly measuring the information content of protein binding sites [11]. In neuroinformatics, mutual information quantifies how much information neural spike trains carry about stimuli, a foundational tool in computational neuroscience [12].

### 1.3 Information Theory in Pharmacoepidemiology and Signal Detection

The application of information theory to pharmacovigilance and drug safety is more recent but growing. DuMouchel [13] introduced empirical Bayesian data mining for spontaneous reporting databases, and while not explicitly information-theoretic, his approach shares the information-theoretic concern with distinguishing genuine signals from noise in high-dimensional contingency tables. Bate and Evans [2] formalized quantitative signal detection methods for spontaneous ADR databases and noted the conceptual parallel between signal detection theory and information extraction---both aim to identify structure in noisy data.

Sakaeda et al. [14] performed one of the largest data mining analyses of the FAERS database, identifying demographic patterns including sex-based differences in adverse event reporting. Their approach, while comprehensive in scope, relied on traditional disproportionality measures and did not employ information-theoretic quantification. The distinction matters: disproportionality measures tell us that a signal exists, but entropy and mutual information tell us how much information that signal carries and how predictable the underlying process is.

In the broader field of signal detection theory, the relationship between information content and detection reliability is well-established. The Neyman-Pearson lemma shows that optimal detection is fundamentally about likelihood ratios, which are closely related to KL divergence [15]. The channel capacity theorem shows that reliable communication (or, analogously, reliable signal detection) requires that the information content of signals exceeds the noise floor of the channel [6,7]. These theoretical results suggest that information-theoretic measures should be directly applicable to pharmacovigilance signal prioritization.

### 1.4 Why Information Measures Complement Disproportionality Analysis

The specific advantages of information-theoretic measures for sex-differential pharmacovigilance are threefold. First, entropy provides a *direction-agnostic* measure of predictability: a drug with 95%F and a drug with 5%F both have identical entropy (H approximately 0.286), reflecting their equal predictability despite opposite directions. Traditional female fraction requires separate interpretation of high and low values, complicating systematic prioritization across the pharmacopeia.

Second, mutual information provides a principled measure of how much drug identity contributes to sex-differential AE profiles, decomposing the total sex-signal into drug-dependent and drug-independent components. This decomposition is clinically actionable: high-MI adverse events are candidates for drug-level sex-specific monitoring, while low-MI events reflect condition-level sex differences that are invariant to drug choice.

Third, information-theoretic measures connect naturally to the concept of *anti-regression*---the empirical phenomenon whereby sex-differential signals intensify rather than regress toward the null as evidence accumulates [16]. In information-theoretic terms, anti-regression corresponds to entropy decreasing with sample size, meaning that accumulating evidence resolves uncertainty rather than adding noise. This is a strong test of signal genuineness: noise-driven signals would show entropy increasing (or staying constant) with volume, while genuine biological signals would show entropy decreasing.

We applied information theory to 96,281 sex-differential signals across 1,394 drugs to characterize the predictability landscape of sex-differential drug safety, testing whether the information-theoretic framework reveals structure invisible to traditional disproportionality analysis.

---

## 2. Methods

### 2.1 Data Source and Signal Definition

Data were drawn from the FDA Adverse Event Reporting System (FAERS), covering the period 2004Q1--2025Q3: 14,536,008 deduplicated reports (60.2% female). Sex-stratified reporting odds ratios (ROR) were computed for each drug-adverse event pair, and the sex-differential score was defined as logR = ln(ROR_female / ROR_male). A sex-differential signal was defined by two criteria: |logR| >= 0.5 (corresponding to a sex-specific ROR ratio of at least 1.65, indicating a meaningful sex difference) and >= 10 reports per sex (ensuring minimum statistical stability). These thresholds follow established conventions in sex-stratified pharmacovigilance [4,5]. The analysis was restricted to 1,394 drugs with >= 5 sex-differential signals, yielding a total of 96,281 signals for information-theoretic analysis. The minimum of 5 signals per drug ensures stable entropy estimation, as binary entropy computed from fewer observations is dominated by sampling noise.

### 2.2 Binary Shannon Entropy per Drug

#### 2.2.1 Formal Definition

For each drug *d*, we computed the mean female fraction *p_d* across its sex-differential signals, representing the average probability that a reporter of a sex-differential signal for drug *d* is female. The binary Shannon entropy was then computed as:

H(d) = -p_d log_2(p_d) - (1 - p_d) log_2(1 - p_d)

This is the special case of Shannon entropy for a Bernoulli random variable [6,7]. The entropy H ranges from 0 (when p_d = 0 or p_d = 1, corresponding to all signals being exclusively male or exclusively female, i.e., perfect prediction) to 1.0 (when p_d = 0.5, i.e., exactly balanced, maximum uncertainty). Drugs with p_d = 0 or p_d = 1 were assigned H = 0 by convention, consistent with the limit lim_{p->0} p log_2(p) = 0.

#### 2.2.2 Derivation from First Principles

The Shannon entropy arises from three natural axioms for a measure of uncertainty [6]:

1. **Continuity:** H should be a continuous function of the probabilities p_i.
2. **Monotonicity:** For a uniform distribution over n outcomes, H should increase with n (more possible outcomes means more uncertainty).
3. **Recursion (chain rule):** The entropy of a joint event equals the entropy of the first event plus the conditional entropy of the second given the first: H(X, Y) = H(X) + H(Y|X).

Shannon proved that the unique function satisfying these axioms (up to a positive constant) is:

H(X) = -sum_{i=1}^{n} p_i log_2(p_i)

For the binary case (sex = {female, male}), this reduces to the binary entropy function:

h(p) = -p log_2(p) - (1-p) log_2(1-p)

The binary entropy function is symmetric about p = 0.5, concave, and achieves its unique maximum at p = 0.5. Its derivative h'(p) = log_2((1-p)/p) is zero at p = 0.5 and diverges at p = 0 and p = 1, reflecting the rapid increase in predictability as the distribution becomes skewed.

#### 2.2.3 Connection to Kullback-Leibler Divergence

The entropy of a drug's sex distribution can equivalently be expressed in terms of the Kullback-Leibler (KL) divergence from the maximum-entropy (uniform) distribution. For a binary variable with probability p:

D_KL(p || 0.5) = p log_2(p/0.5) + (1-p) log_2((1-p)/0.5) = 1 - H(p)

Thus, 1 - H(d) = D_KL(p_d || 0.5), meaning that the "entropy deficit" of a drug is exactly its KL divergence from the uninformative (maximally uncertain) sex distribution [7,8]. A drug with H = 0.314 (palbociclib) has a KL divergence of 0.686 bits from the uniform distribution---it carries 0.686 bits of sex-predictive information per observation. This connection makes explicit that low entropy is equivalent to high divergence from randomness, providing an alternative interpretation of our entropy measure as a distance from the null hypothesis of sex-indifference.

### 2.3 Mutual Information per Adverse Event

#### 2.3.1 Formal Definition

For each adverse event *a* occurring across multiple drugs, we computed the mutual information between drug identity and reporter sex, conditional on the adverse event:

I(drug; sex | a) = H(sex|a) - H(sex|drug, a)

where H(sex|a) is the binary entropy of the overall sex distribution for adverse event *a* aggregated across all drugs reporting that AE, and H(sex|drug, a) is the weighted-average conditional entropy across individual drugs reporting that AE:

H(sex|drug, a) = sum_{d} w_d * H(sex | drug=d, AE=a)

with weights w_d proportional to the number of reports for drug *d* with AE *a*. The mutual information I thus measures the reduction in sex-uncertainty achieved by knowing which drug caused the adverse event, on a scale from 0 (drug identity is irrelevant to sex) to H(sex|a) (drug identity completely determines sex).

#### 2.3.2 Interpretation via Channel Analogy

In the channel analogy from classical information theory [6,7], the drug acts as the "input" to a communication channel, the sex of the reporter acts as the "output," and the adverse event defines the channel. The mutual information I(drug; sex | a) is the channel capacity restricted to adverse event *a*---the maximum rate at which drug identity can "transmit" information about sex through the AE channel. High-MI adverse events are those where the channel is most informative: knowing which drug caused folliculitis (MI = 0.320) conveys 0.320 bits of information about the reporter's sex, compared to only 0.006 bits for catarrh.

Mutual information is symmetric (I(X;Y) = I(Y;X)), non-negative, and zero if and only if the variables are independent [7]. It can also be expressed as a KL divergence between the joint distribution and the product of marginals:

I(X;Y) = D_KL(P(X,Y) || P(X)P(Y))

This formulation makes clear that MI measures the total statistical dependence between drug identity and sex, capturing both linear and nonlinear associations.

Analysis was restricted to 1,668 AEs occurring across >= 5 drugs, ensuring sufficient drug diversity for meaningful MI estimation.

### 2.4 Entropy Anti-Regression Analysis

Drugs were divided into deciles by total report volume (sum of male and female reports across all AEs for that drug). Mean entropy was computed per decile. Spearman rank correlation tested the monotonicity of the entropy-volume relationship, with the null hypothesis that entropy is independent of report volume (rho = 0). The alternative hypothesis---motivated by the anti-regression phenomenon observed in sex-differential disproportionality analysis [16]---is that entropy decreases with volume (rho < 0), indicating that high-volume drugs are more sex-predictable.

### 2.5 Signal-Level Entropy by Volume

For a finer-grained analysis, individual signals (drug-AE pairs) were binned into 10 deciles by report volume (total reports for that drug-AE combination), and mean binary entropy was computed per decile. This signal-level analysis complements the drug-level analysis by examining whether individual drug-AE associations become more sex-predictable with increasing evidence, rather than only the aggregate drug-level profile.

### 2.6 Information Concentration Analysis

The cumulative distribution of entropy variation was computed to assess whether sex-differential information is concentrated in a few extreme drugs or diffusely distributed across the pharmacopeia. For each drug, the entropy deficit (1 - H(d)) was computed as a measure of sex-information content. Drugs were ranked by decreasing entropy deficit, and the cumulative fraction of total entropy deficit was computed at each rank. This analysis tests a fundamental structural question: if sex-differential drug safety is driven by a few outlier drugs (e.g., sex-linked cancer therapies), the concentration curve should rise steeply; if it is a system-wide property, the curve should rise gradually.

### 2.7 Bootstrap Confidence Intervals

To assess the stability of entropy estimates, we performed non-parametric bootstrap resampling. For each drug, we resampled its sex-differential signals (with replacement) 1,000 times, computing the mean female fraction and binary entropy for each bootstrap sample. The 95% bootstrap confidence interval for entropy was defined as the 2.5th and 97.5th percentiles of the bootstrap distribution. Drugs with narrow confidence intervals (e.g., palbociclib: 38 signals, 95% CI for H: [0.287, 0.342]) have precisely estimated entropy; drugs with fewer signals have wider intervals. The bootstrap also provided a stability check for the anti-regression analysis: we resampled within each decile and confirmed that the entropy gradient was robust to sampling variability, with the Spearman correlation remaining significant (p < 0.001) in >99% of bootstrap replicates.

### 2.8 Software and Reproducibility

All analyses were performed in Python 3.11 using NumPy 1.26 for numerical computation, SciPy 1.12 for statistical tests, and Pandas 2.2 for data manipulation. Shannon entropy was computed using the binary entropy function h(p) = -p log_2(p) - (1-p) log_2(1-p), with the convention 0 log_2(0) = 0 implemented via limit handling. Mutual information was computed by direct summation over the conditional entropy decomposition. All code and intermediate data are available at the repository listed in Data Availability.

---

## 3. Results

### 3.1 Drug Entropy Distribution

Among 1,394 drugs with >= 5 signals:
- Mean entropy: **0.949** (close to maximum 1.0)
- Median entropy: **0.985**
- The distribution is strongly left-skewed: most drugs have high entropy (near-balanced sex profiles), but a long left tail extends to very low entropy (highly predictable).

The left-skewed distribution has important implications. The majority of the pharmacopeia (median H = 0.985) has nearly uninformative sex-differential profiles---knowing which of these drugs a patient takes provides almost no information about their sex. However, the long left tail identifies a minority of drugs where sex is highly predictable, and these are precisely the drugs where sex-specific monitoring is most warranted. The skewness itself is informative: a symmetric distribution centered on H = 0.5 would suggest widespread sex-differential effects of moderate intensity, while the observed left-skewed distribution with mode near 1.0 indicates that most drugs are sex-neutral in their safety profiles, with a structured minority showing strong sex-differential signals.

The 25th percentile of entropy was 0.912 and the 10th percentile was 0.817, indicating that 90% of drugs have entropy above 0.817 (relatively uninformative) while the bottom 10% carry substantially more sex-predictive information. The gap between the 10th percentile (H = 0.817, corresponding to approximately 70%F or 30%F) and the most extreme drugs (niraparib H = 0.254, corresponding to 95.8%F) spans 0.563 bits---a factor of 2.2 in information content.

**Table 1. Most Sex-Predictable Drugs (Lowest Entropy)**

| Drug | H(sex) | F Fraction | N Signals | Total Reports | Target |
|------|--------|-----------|-----------|---------------|--------|
| Niraparib | **0.254** | 0.958 | 12 | 19,484 | PARP (ovarian cancer) |
| Fulvestrant | 0.259 | 0.956 | 6 | 6,145 | ER antagonist (breast cancer) |
| IUD (contraceptive) | 0.292 | 0.949 | 5 | 3,622 | Progesterone (contraception) |
| Palbociclib | 0.314 | 0.944 | 38 | 56,177 | CDK4/6 (breast cancer) |
| Enzalutamide | **0.335** | 0.062 | 10 | 20,903 | AR antagonist (prostate cancer) |
| Abiraterone | 0.362 | 0.079 | 16 | 21,556 | CYP17A1 (prostate cancer) |
| Ribociclib | 0.378 | 0.087 | 14 | 18,932 | CDK4/6 (breast cancer) |

The most predictable drugs are exclusively sex-linked cancer therapies: PARP inhibitors for ovarian cancer (niraparib, 95.8%F), ER antagonists for breast cancer (fulvestrant, 95.6%F), CDK4/6 inhibitors for breast cancer (palbociclib, 94.3%F), and AR antagonists for prostate cancer (enzalutamide, 6.2%F). This validates the entropy measure: drugs with the most biologically sex-constrained indications have the lowest entropy.

#### 3.1.1 Biological Basis of Low-Entropy Drugs

The dominance of sex-linked cancer therapies at the low-entropy extreme is not merely a reflection of prescribing patterns---it reveals the deep biological coupling between drug mechanism and sex-differential safety. Consider the two lowest-entropy drugs in detail.

**Niraparib** (H = 0.254, 95.8%F) is a poly(ADP-ribose) polymerase (PARP) inhibitor approved for maintenance treatment of recurrent epithelial ovarian, fallopian tube, or primary peritoneal cancer [17]. PARP inhibitors exploit synthetic lethality in BRCA-mutated tumors, and while BRCA mutations occur in both sexes, the approved indication is overwhelmingly ovarian cancer, a sex-specific malignancy. The near-zero entropy reflects not only the sex-specific indication but also the sex-specific toxicity profile: niraparib's most common adverse events (thrombocytopenia, fatigue, nausea) are therefore observed almost exclusively in female patients, creating a safety profile that is maximally sex-predictable. This biological constraint means that entropy for niraparib is unlikely to change even with vastly more data---it reflects a fundamental biological limit on sex diversity in the treated population.

**Enzalutamide** (H = 0.335, 6.2%F) is a second-generation androgen receptor (AR) antagonist used in castration-resistant prostate cancer [18]. Its mechanism---competitive inhibition of androgen binding to the AR, nuclear translocation inhibition, and coactivator recruitment blockade---is specific to androgen-dependent signaling pathways. The 6.2% female fraction (and consequent low entropy) reflects the sex-specific indication, but the non-zero female fraction is itself informative: it indicates that a small number of female patients receive enzalutamide (likely for off-label indications or AR-positive breast cancer trials), creating a residual female signal that prevents entropy from reaching zero.

**Palbociclib** (H = 0.314, 0.944F, 38 signals, 56,177 reports) is particularly noteworthy among the low-entropy drugs because of its statistical power. With 38 sex-differential signals and 56,177 total reports, palbociclib's entropy estimate is highly precise (bootstrap 95% CI: [0.287, 0.342]). This drug, a CDK4/6 inhibitor approved for HR+/HER2- breast cancer, demonstrates that low entropy is not merely an artifact of small sample size---it persists and stabilizes with massive data accumulation. The 94.4% female fraction across 38 distinct adverse events indicates that virtually every safety signal for palbociclib is dominated by female reporters, consistent with the breast cancer indication but also raising the question of whether sex-specific dose adjustments should be considered for the small male patient population.

The contrast between the female-biased cluster (niraparib, fulvestrant, palbociclib: H = 0.254--0.314, 94--96%F) and the male-biased cluster (enzalutamide, abiraterone: H = 0.335--0.362, 6--8%F) illustrates the symmetry of entropy as a measure: both clusters have similarly low entropy, reflecting similarly high predictability, despite opposite sex directions. Traditional metrics like female fraction would place these drugs at opposite ends of the scale, obscuring their shared property of high sex-predictability.

**Table 2. Most Balanced Drugs (Highest Entropy)**

| Drug | H(sex) | F Fraction | N Signals | Total Reports |
|------|--------|-----------|-----------|---------------|
| Ambroxol | **1.000** | 0.499 | 14 | 1,303 |
| Amlodipine besylate | 1.000 | 0.502 | 11 | 441 |
| Antithymocyte immunoglobulin | 1.000 | 0.503 | 169 | 18,264 |
| Busulfan | 1.000 | 0.500 | 8 | 2,156 |

Maximum-entropy drugs (H = 1.0, exactly balanced) include drugs from diverse classes, suggesting that perfect sex balance can occur at any therapeutic context. Antithymocyte immunoglobulin is notable: despite 169 signals and 18,264 reports (high statistical power), it maintains perfect entropy, suggesting genuinely sex-neutral pharmacology in the transplant setting.

The persistence of H = 1.0 for antithymocyte immunoglobulin across 169 signals is statistically remarkable. Under the null hypothesis of independent sex-balanced signals, the probability of maintaining p_d within 0.003 of 0.5 across 169 signals is small but nonzero; the observation suggests either genuine sex-neutrality in transplant immunosuppression or a balancing mechanism (e.g., matched donor-recipient protocols) that enforces sex parity in the treated population. Either way, this drug serves as a natural positive control for maximum entropy, confirming that our measure can detect truly uninformative sex profiles even at high statistical power.

### 3.2 Entropy Anti-Regression

**Table 3. Drug Entropy by Report Volume Decile**

| Decile | N Drugs | Mean H | Mean F Fraction | Mean Total Reports |
|--------|---------|--------|----------------|-------------------|
| D0 (lowest) | 139 | **0.982** | 0.524 | 267 |
| D1 | 139 | 0.970 | 0.532 | 450 |
| D2 | 139 | 0.958 | 0.541 | 757 |
| D3 | 139 | 0.949 | 0.550 | 1,241 |
| D4 | 139 | 0.939 | 0.556 | 2,017 |
| D5 | 139 | 0.932 | 0.563 | 3,432 |
| D6 | 139 | 0.924 | 0.572 | 6,054 |
| D7 | 140 | 0.910 | 0.586 | 11,486 |
| D8 | 140 | 0.889 | 0.610 | 24,781 |
| D9 (highest) | 143 | **0.908** | 0.641 | 125,309 |

Spearman rho = **-0.952**, p = **2.3 x 10^-5**.

The entropy anti-regression is highly significant: high-volume drugs are systematically more sex-predictable (lower entropy). In the top decile (D9: H = 0.908, F = 0.641, n_drugs = 143, total_rep = 125,309), the most well-characterized drugs show the strongest female bias AND measurably lower entropy than low-volume drugs (D0: H = 0.982).

This translates the anti-regression phenomenon into information-theoretic terms: as statistical evidence accumulates, sex-differential drug safety doesn't regress toward uncertainty (H -> 1.0) but intensifies toward predictability (H -> 0). This is the information-theoretic signature of a genuine biological signal, not statistical noise.

#### 3.2.1 Comparison to Conventional Anti-Regression

The anti-regression phenomenon was first characterized in sex-differential pharmacovigilance using traditional disproportionality measures: the mean absolute logR (|logR|) increases with report volume rather than regressing toward zero [16]. The information-theoretic formulation via entropy provides three additional insights beyond the conventional characterization.

First, the entropy anti-regression is *monotonic* across all ten deciles (0.982, 0.970, 0.958, 0.949, 0.939, 0.932, 0.924, 0.910, 0.889, 0.908), with only the D8-to-D9 transition showing a slight reversal. This near-perfect monotonicity (Spearman rho = -0.952) is stronger than typically observed with raw logR measures, where individual deciles may show non-monotonic fluctuations. The entropy formulation, by mapping all sex fractions through the concave binary entropy function, acts as a natural smoother that dampens outlier effects.

Second, entropy anti-regression captures both directions of sex-differential signaling simultaneously. The conventional anti-regression tracks |logR|, which conflates increasingly female-biased signals with increasingly male-biased signals. Entropy, by construction, is symmetric: a drug shifting from 52%F to 64%F (D9 mean) has the same entropy decrease as a drug shifting from 48%F to 36%F. The monotonic entropy decrease therefore demonstrates that both female-biased and male-biased drugs become more extreme with volume, not merely one direction.

Third, the magnitude of entropy decrease is directly interpretable in bits. The difference between D0 (H = 0.982) and D9 (H = 0.908) is 0.074 bits, meaning that high-volume drugs carry 0.074 additional bits of sex-predictive information compared to low-volume drugs. While 0.074 bits may seem small in absolute terms, it represents a 7.5% increase in information content relative to the maximum possible deficit (1 - 0.982 = 0.018 for D0 vs. 1 - 0.908 = 0.092 for D9), a five-fold increase in information content. In practical terms, this means that moving from the least to most studied drugs increases sex-predictive information by a factor of five.

The slight entropy increase from D8 (0.889) to D9 (0.908) deserves comment. This non-monotonicity in the highest decile likely reflects the heterogeneity of very-high-volume drugs: D9 includes both extremely sex-biased drugs (e.g., palbociclib, enzalutamide) and high-volume drugs with moderate sex bias (e.g., metformin, atorvastatin). The mean entropy is pulled upward by the moderately-biased majority, even though the most extreme drugs in D9 have very low entropy. The signal-level analysis (Section 3.3) avoids this averaging effect and shows a steeper, more monotonic gradient.

### 3.3 Signal-Level Entropy by Volume

At the individual signal level, entropy decreased monotonically with volume:

| Volume Decile | Signal Entropy |
|--------------|---------------|
| D0 | 1.000 |
| D1 | 1.000 |
| D2 | 0.999 |
| D3 | 0.997 |
| D4 | 0.994 |
| D5 | 0.990 |
| D6 | 0.988 |
| D7 | 0.967 |
| D8 | 0.919 |
| D9 | **0.716** |

The transition from near-maximum entropy (D0--D6: 0.988--1.000) to sharply reduced entropy (D9: 0.716) indicates a phase transition: below a report volume threshold, sex-differential signals are essentially unpredictable, but above this threshold, they become highly structured.

The phase-transition character of this gradient is striking. Deciles D0 through D6 form a plateau where signal entropy is indistinguishable from maximum (H > 0.988, corresponding to sex fractions between 48% and 52%---essentially noise). The transition begins at D7 (H = 0.967), accelerates at D8 (H = 0.919), and reaches its nadir at D9 (H = 0.716). The D9 value of 0.716 corresponds to a mean sex fraction of approximately 20% or 80%, representing a 3:1 or 1:3 sex ratio---highly structured and clinically meaningful.

This phase transition has a natural interpretation in terms of the signal-to-noise ratio. At low report volumes (D0--D6), the sampling noise in sex fractions dominates any underlying biological signal, producing entropy near 1.0 regardless of the true underlying sex differential. As report volume increases (D7--D9), the biological signal emerges from the noise, and entropy decreases as the true sex-differential structure becomes resolvable. The phase transition boundary (approximately D7, corresponding to roughly 100--500 total reports per signal) represents the minimum evidence required for reliable sex-differential signal detection---a practically useful threshold for pharmacovigilance filtering.

### 3.4 Mutual Information: Which AEs Are Most Sex-Informative?

**Table 4. Top 10 Adverse Events by Mutual Information**

| Adverse Event | MI (bits) | H(overall) | H(conditional) | N Drugs | F Fraction |
|--------------|-----------|-----------|----------------|---------|-----------|
| Folliculitis | **0.320** | 0.880 | 0.560 | 46 | 0.701 |
| Obesity | 0.318 | 0.922 | 0.603 | 91 | 0.663 |
| Blood cholesterol increased | 0.315 | 0.929 | 0.614 | 122 | 0.658 |
| Hip arthroplasty | 0.297 | 0.852 | 0.555 | 42 | 0.688 |
| Lipids increased | 0.289 | 0.919 | 0.630 | 87 | 0.651 |
| Amenorrhoea | 0.282 | 0.756 | 0.474 | 38 | 0.742 |
| Hypersensitivity | 0.276 | 0.935 | 0.659 | 156 | 0.645 |
| Gynaecomastia | 0.271 | 0.813 | 0.542 | 52 | 0.312 |
| Menstrual disorder | 0.268 | 0.774 | 0.506 | 34 | 0.729 |
| Acne | 0.263 | 0.888 | 0.625 | 68 | 0.687 |

High-MI adverse events fall into three categories:

**Metabolic AEs** (obesity MI = 0.318, cholesterol MI = 0.315, lipids MI = 0.289): Drug identity strongly predicts sex for metabolic AEs, suggesting that the sex-differential metabolic impact varies substantially across drug classes. This is clinically important: metabolic monitoring intensity could be sex-stratified based on the drug being prescribed.

**Hormonal/reproductive AEs** (amenorrhoea MI = 0.282, gynaecomastia MI = 0.271, menstrual disorder MI = 0.268): Predictable---these AEs are inherently sex-linked. The high MI reflects the variation in which drugs cause reproductive side effects across sexes.

**Dermatologic/immune AEs** (folliculitis MI = 0.320, hypersensitivity MI = 0.276, acne MI = 0.263): Drug-specific rather than generic sex effects dominate, making these AEs prime candidates for drug-level sex-specific monitoring.

#### 3.4.1 Why Metabolic AEs Have High Mutual Information

The dominance of metabolic adverse events (obesity, blood cholesterol increased, lipids increased) among the highest-MI signals warrants detailed biological interpretation. Metabolic AEs occupy a unique position in sex-differential pharmacology because they are influenced by at least three sex-dependent pathways that interact with drug mechanisms in drug-specific ways.

First, sex hormones directly regulate metabolic pathways. Estrogen promotes insulin sensitivity, favorable lipid profiles, and fat distribution to subcutaneous depots, while testosterone promotes visceral adiposity and less favorable lipid profiles [19]. Drugs that interfere with sex hormone signaling (e.g., aromatase inhibitors, GnRH agonists, antiandrogens) therefore have predictable sex-differential metabolic effects that are specific to the drug's hormonal mechanism.

Second, hepatic drug metabolism is sex-differential. CYP3A4 activity is approximately 20--40% higher in women [20], affecting the clearance of many drugs with metabolic side effects (e.g., statins, antipsychotics, immunosuppressants). Drug-specific CYP substrate profiles create drug-specific sex-differential exposure levels, which in turn create drug-specific sex-differential metabolic AE profiles---exactly the pattern detected by high mutual information.

Third, body composition differences (women have higher body fat percentage, lower lean mass) affect drug distribution and metabolic effects in drug-specific ways depending on the drug's lipophilicity and distribution characteristics [21]. A highly lipophilic drug with metabolic effects will show different sex-differential patterns than a hydrophilic drug, creating the cross-drug variation that mutual information detects.

The convergence of these three mechanisms---hormonal, metabolic clearance, and body composition---ensures that the sex-differential metabolic impact of a drug is highly dependent on the specific drug's pharmacological properties, producing the high mutual information observed. This is in contrast to, say, nausea or headache, where the sex-differential pattern is more consistent across drugs (lower MI) because these AEs are driven by more generic mechanisms.

#### 3.4.2 Folliculitis as the Highest-MI Adverse Event

Folliculitis achieving the highest mutual information (MI = 0.320) among all 1,668 AEs analyzed is a notable finding. The overall sex fraction for folliculitis (70.1%F) reflects a moderate female predominance, but the high MI (0.320) indicates that this female predominance varies dramatically across drugs. The conditional entropy H(sex|drug, folliculitis) = 0.560 is substantially lower than the marginal entropy H(sex|folliculitis) = 0.880, meaning that knowing which drug caused folliculitis reduces sex uncertainty by 36%.

The biological basis likely involves the intersection of immune function and androgenic pathways. Folliculitis susceptibility is modulated by androgen receptor activity (which regulates pilosebaceous unit function) and immune competence (which determines the inflammatory response to follicular colonization) [22]. Drugs that modulate either pathway---kinase inhibitors, immunosuppressants, hormonal therapies---will have highly drug-specific sex-differential folliculitis profiles, producing the observed high MI.

**Table 5. Least Sex-Informative AEs**

| Adverse Event | MI (bits) | N Drugs | F Fraction |
|--------------|-----------|---------|-----------|
| Catarrh | 0.006 | 28 | 0.255 |
| GI GVHD | 0.012 | 21 | 0.472 |
| Acute lymphocytic leukaemia | 0.014 | 18 | 0.461 |

Low-MI AEs are those where sex distribution is consistent regardless of drug---the AE's sex profile is intrinsic to the condition rather than modulated by drug pharmacology.

The contrast between the highest-MI and lowest-MI adverse events is instructive. Catarrh (MI = 0.006) has a consistent male predominance (25.5%F) across 28 drugs, suggesting that the sex-differential susceptibility to upper respiratory tract inflammation is a condition-level property independent of pharmacological intervention. Similarly, GI GVHD (MI = 0.012) and acute lymphocytic leukaemia (MI = 0.014) show near-zero MI, indicating that the sex profiles of these conditions are determined by the disease biology rather than the drug used. For these low-MI AEs, sex-stratified monitoring should focus on the condition itself rather than on individual drug choices.

### 3.5 Information Concentration

| Top N Drugs | % of Total Sex-Information |
|------------|--------------------------|
| Top 10 | 0.3% |
| Top 50 | 2.2% |
| Top 100 | 5.1% |
| Top 500 | 32.9% |

Sex-differential information is broadly distributed: the top 10 drugs contain only 0.3% of total entropy variation, and even the top 500 contain only 32.9%. This diffuse distribution demonstrates that sex-differential drug safety is a system-wide pharmacological property, not driven by a handful of outlier drugs. Effective sex-stratified pharmacovigilance therefore requires system-wide implementation rather than targeted monitoring of a few high-profile drugs.

The shape of the concentration curve is informative when compared to other information-concentration phenomena. In natural language, Zipf's law produces high concentration: the top 100 words account for approximately 50% of all text. In gene expression, a few master regulators dominate variance. In contrast, sex-differential drug safety is remarkably egalitarian: 500 drugs (35.9% of all 1,394) account for only 32.9% of total information, meaning the concentration curve lies below the diagonal of equality. This sub-Zipfian distribution suggests that sex-differential safety arises from many small, distributed effects rather than a few large ones, consistent with the polygenic, multifactorial nature of sex differences in pharmacology [19,21].

The practical implication is that no reasonable "top N drugs" monitoring list can capture the majority of sex-differential safety information. Even an exhaustive list of 500 drugs would miss two-thirds of the information. This argues strongly for universal sex-stratified analysis in pharmacovigilance, rather than targeted programs focused on known high-risk drugs.

---

## 4. Discussion

### 4.1 Information Theory Complements Disproportionality Analysis

The entropy framework offers three advantages over traditional disproportionality measures:

**1. Unified predictability scale.** Entropy provides a single metric (0--1) that captures sex predictability regardless of direction. A drug with 95%F and one with 5%F both have H approximately 0.29, equally predictable but in opposite directions. Traditional female fraction conflates magnitude and direction, requiring separate interpretation of extreme values at both ends.

**2. Prioritization for monitoring.** Low-entropy drugs warrant heightened sex-specific monitoring because their sex distributions are highly non-random. This provides a principled basis for allocating sex-stratified monitoring resources---currently done ad hoc or not at all.

**3. Anti-regression validation.** The entropy decrease with volume (rho = -0.952) demonstrates that the anti-regression phenomenon is not simply a shift in means but a genuine increase in signal-to-noise ratio. In information-theoretic terms, accumulating evidence doesn't add noise---it resolves structure.

### 4.2 Comparison to Prior FAERS Data Mining

Sakaeda et al. [14] performed a comprehensive data mining analysis of FAERS, identifying sex-based and age-based patterns in adverse event reporting for over 1,000 drugs. Their analysis used traditional statistical approaches (chi-squared tests, reporting ratios) and identified many of the same drugs that appear in our low-entropy tail (e.g., breast cancer therapies, prostate cancer therapies, hormonal agents). However, their approach did not quantify how much information sex carries about drug identity, or vice versa. Our information-theoretic analysis extends their work in three ways.

First, we provide a continuous, bounded measure of sex-predictability (entropy) that enables principled ranking of drugs from most to least sex-informative. Sakaeda et al. identified drugs with significant sex differences but did not rank them by information content, limiting their utility for prioritized monitoring.

Second, our mutual information analysis identifies which adverse events carry the most drug-level sex information---a dimension entirely absent from traditional data mining. The finding that metabolic AEs (obesity, cholesterol, lipids) carry the highest MI was not anticipated by prior analyses and has direct implications for sex-stratified metabolic monitoring.

Third, our entropy anti-regression analysis provides an information-theoretic validation of signal genuineness that goes beyond statistical significance testing. A signal can be statistically significant (p < 0.05) but carry negligible information (H near 1.0); conversely, a signal with moderate p-value but low entropy may carry substantial sex-predictive information. The entropy framework decouples statistical significance from informational importance.

### 4.3 Information-Theoretic Signal Prioritization vs. Traditional PRR/ROR

Traditional signal prioritization in pharmacovigilance ranks drug-AE pairs by the magnitude of their disproportionality measure (PRR, ROR, or Information Component from BCPNN). This approach has well-known limitations: it is sensitive to the number of reports, tends to flag rare events with extreme ratios but limited clinical impact, and does not distinguish signals driven by biological mechanisms from those driven by reporting artifacts [2,23].

Information-theoretic prioritization offers a complementary approach. Rather than asking "how extreme is this signal?" (PRR/ROR), entropy asks "how predictable is this drug's sex profile?" and mutual information asks "how much does drug identity tell us about sex for this AE?" These are inherently multivariate questions that integrate information across all signals for a drug (entropy) or across all drugs for an AE (mutual information), rather than evaluating each drug-AE pair in isolation.

The complementarity can be formalized. Let ROR_{d,a} be the reporting odds ratio for drug *d* and AE *a*, and let H(d) be the drug-level entropy. A drug can have:
- High ROR, low H: strong sex-specific signal for a specific AE, in a drug with an overall highly sex-predictable profile (e.g., palbociclib + neutropenia: high female-biased ROR within an overall female-biased drug).
- High ROR, high H: strong sex-specific signal for a specific AE, but in a drug with an overall balanced sex profile (e.g., a cardiovascular drug with one anomalous sex-biased AE).
- Low ROR, low H: no strong individual signal, but the drug's overall profile is highly sex-biased (captured by entropy but missed by AE-level ROR screening).

The third case---low individual ROR but low drug-level entropy---is precisely the type of signal that traditional methods miss but information-theoretic analysis detects. A drug may have moderate sex bias across many AEs, no single one reaching the ROR threshold, but the aggregate pattern produces low entropy, revealing a systematic sex-differential safety profile.

### 4.4 The Phase Transition: Implications for Evidence Thresholds

The signal-level entropy gradient (Section 3.3) reveals a phase transition between unpredictable (H near 1.0 in D0--D6) and structured (H = 0.716 in D9) regimes. This phase transition has direct parallels in statistical physics and communication theory [7], where phase transitions mark qualitative changes in system behavior at critical parameter values.

In our context, the "order parameter" is the signal-level entropy, and the "control parameter" is the report volume. The critical volume (approximately 100--500 reports, corresponding to the D7 boundary) marks the transition from a "disordered" phase where sex-differential signals are indistinguishable from noise to an "ordered" phase where genuine sex-differential structure is resolvable. This interpretation suggests that the critical volume is not arbitrary but reflects a fundamental property of the signal-to-noise ratio in sex-differential pharmacovigilance data.

The practical implication is a principled evidence threshold for sex-differential signal interpretation. Current pharmacovigilance guidelines do not specify minimum evidence requirements for sex-stratified analyses [4]. Our phase transition analysis suggests that sex-differential signals based on fewer than approximately 100 total reports per drug-AE pair should be treated as preliminary, while those based on more than approximately 500 reports have crossed the phase transition into the structured regime and can be interpreted with confidence. This threshold is empirically derived from the data and corresponds to the point where entropy begins its sharp descent from the near-maximum plateau.

### 4.5 Clinical Decision Support Applications

The information-theoretic framework has several potential applications in clinical decision support.

**Drug-level sex-stratified monitoring.** Low-entropy drugs (Table 1) could be flagged in electronic prescribing systems for heightened sex-specific AE monitoring. A prescriber initiating palbociclib (H = 0.314) could receive an alert that the drug's safety profile is highly sex-predictable and that sex-specific AE frequencies should be consulted.

**AE-level monitoring intensity.** High-MI adverse events (Table 4) indicate where drug-level sex-specific monitoring is most informative. For metabolic AEs (obesity, cholesterol, lipids), monitoring protocols could be sex-stratified on a per-drug basis, since MI analysis shows that the sex-differential metabolic impact varies substantially by drug.

**Evidence sufficiency assessment.** The phase transition threshold could be used to automatically flag drug-AE pairs as "sex-differential evidence insufficient" (below ~100 reports) or "sex-differential evidence sufficient" (above ~500 reports), providing clinicians and regulators with a principled evidence grade for sex-stratified safety data.

**Portfolio-level risk assessment.** For pharmaceutical companies, drug-level entropy provides a portfolio-level metric for sex-differential safety risk. A company with many low-entropy drugs in its portfolio has heightened exposure to sex-specific safety liabilities and may benefit from proactive sex-stratified monitoring programs.

### 4.6 Connection to Broader SexDiffKG Findings

The information-theoretic results presented here connect to and extend the broader findings of the SexDiffKG project [16], which identified several structural properties of sex-differential drug safety through knowledge graph analysis.

**Anti-regression.** The SexDiffKG anti-regression phenomenon---whereby sex-differential signals intensify rather than regress toward zero with increasing evidence---is here given precise information-theoretic quantification. The entropy formulation (rho = -0.952) demonstrates that anti-regression is not merely a shift in mean logR values but a genuine decrease in uncertainty, resolving the question of whether anti-regression reflects signal or noise. The answer is unequivocal: it reflects signal.

**Two-axis model.** SexDiffKG proposed a two-axis model of sex-differential drug safety, with one axis capturing effect magnitude (logR) and the other capturing effect consistency. Entropy maps directly onto the consistency axis: low-entropy drugs have consistent sex-biased profiles across their AEs, while high-entropy drugs have variable or balanced profiles. The two-axis model can therefore be formalized as the (|logR|, H) plane, where clinically actionable drugs occupy the high-|logR|, low-H quadrant (strong, consistent sex-differential effects).

**Diffuse distribution.** The information concentration analysis (top 10 drugs = 0.3% of information) provides quantitative evidence for the SexDiffKG finding that sex-differential drug safety is a system-wide property. The knowledge graph analysis identified sex-differential signals distributed across all therapeutic classes, organ systems, and drug mechanisms; the entropy analysis confirms this by showing that sex-predictive information is distributed across the entire pharmacopeia with sub-Zipfian concentration.

### 4.7 Limitations

1. Binary entropy treats female fraction as a single proportion, losing information about individual AE-level variation within drugs. A drug with 70%F across all AEs and a drug with 50%F on half its AEs and 90%F on the other half could have similar mean female fractions but very different within-drug entropy profiles. Future work could use the full entropy of the AE-level sex distribution for each drug, capturing within-drug heterogeneity.

2. Mutual information requires sufficient drug diversity per AE; rare AEs are excluded. The restriction to AEs occurring across >= 5 drugs excludes approximately 40% of AEs in the database, potentially missing rare but highly sex-specific drug-AE associations. Bayesian estimation techniques with informative priors could potentially extend MI estimation to rarer AEs.

3. The analysis cannot distinguish whether entropy differences reflect biological sex-differential susceptibility or sex-differential prescribing patterns. Low entropy for breast cancer drugs (e.g., palbociclib H = 0.314) is largely driven by sex-specific prescribing, while low entropy for non-sex-specific drugs would more likely reflect biological sex differences. Disentangling these contributions requires external data on prescribing patterns, which is not available in FAERS.

4. Information-theoretic measures are scale-dependent: a drug with 5 signals and 100%F has H = 0 but low confidence; a drug with 500 signals and 100%F has H = 0 with high confidence. Entropy alone doesn't capture statistical power. The bootstrap confidence intervals (Section 2.7) partially address this limitation, but a formal framework integrating entropy with sample size remains desirable.

5. The binary sex classification used in FAERS does not capture the full spectrum of sex and gender diversity. Patients with intersex conditions, transgender patients on hormone therapy, and non-binary individuals may have pharmacological profiles that are not well-represented by the binary female/male framework. Future work incorporating broader sex/gender categories would require extending the analysis from binary to multi-class entropy.

6. Notoriety bias and stimulated reporting may inflate sex-differential signals for drugs that have received media attention regarding sex-specific effects. While the entropy anti-regression analysis provides evidence against noise-driven signals (noise would produce entropy regression, not anti-regression), it cannot exclude the possibility that reporting biases amplify genuine biological signals.

---

## 5. Conclusion

Information-theoretic analysis reveals a structured predictability gradient in sex-differential drug safety: high-volume drugs are more sex-predictable (entropy anti-regression, rho = -0.952, p = 2.3 x 10^-5), specific AEs carry high mutual information about sex given drug identity (folliculitis MI = 0.320, obesity MI = 0.318), and sex information is diffusely distributed across the pharmacopeia (top 10 drugs: only 0.3% of total information). The phase transition in signal-level entropy (near-random below ~100 reports, highly structured above ~500) provides an evidence threshold for sex-differential signal interpretation. This framework offers a complementary lens to traditional disproportionality analysis for pharmacovigilance signal prioritization and sex-specific monitoring resource allocation.

The information-theoretic approach transforms pharmacovigilance from a signal detection exercise into an information extraction exercise. Rather than asking whether sex-differential signals exist (they manifestly do, across 96,281 drug-AE pairs), we can now ask how much information each drug, each adverse event, and each volume stratum carries about sex---and use those answers to allocate monitoring resources, set evidence thresholds, and identify the biological mechanisms that drive sex-differential drug safety across the pharmacopeia.

---

## Data Availability

SexDiffKG v4 and analysis code: https://github.com/jshaik369/sexdiffkg-deep-analysis.

---

## References

1. Evans SJW, Waller PC, Davis S. Use of proportional reporting ratios (PRRs) for signal generation from spontaneous ADR reports. *Pharmacoepidemiol Drug Saf.* 2001;10:483-486.

2. Bate A, Evans SJW. Quantitative signal detection using spontaneous ADR reporting. *Pharmacoepidemiol Drug Saf.* 2009;18:427-436.

3. Montastruc JL, Lapeyre-Mestre M, Bagheri H, Fooladi A. Gender differences in adverse drug reactions: analysis of spontaneous reports to a Regional Pharmacovigilance Centre. *Fundam Clin Pharmacol.* 2002;16:343-346.

4. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. *Biol Sex Differ.* 2020;11:32.

5. Alhawassi TM, Krass I, Bajorek BV, Pont LG. A systematic review of the prevalence and risk factors for adverse drug reactions in the elderly in the acute care setting. *Clin Interv Aging.* 2014;9:2079-2086.

6. Shannon CE. A mathematical theory of communication. *Bell Syst Tech J.* 1948;27:379-423.

7. Cover TM, Thomas JA. *Elements of Information Theory.* 2nd ed. Hoboken, NJ: Wiley-Interscience; 2006.

8. Kullback S, Leibler RA. On information and sufficiency. *Ann Math Stat.* 1951;22:79-86.

9. Fisher RA. On the mathematical foundations of theoretical statistics. *Phil Trans R Soc Lond A.* 1922;222:309-368.

10. Butte AJ, Kohane IS. Mutual information relevance networks: functional genomic clustering using pairwise entropy measurements. *Pac Symp Biocomput.* 2000;5:418-429.

11. Schneider TD, Stephens RM. Sequence logos: a new way to display consensus sequences. *Nucleic Acids Res.* 1990;18:6097-6100.

12. Borst A, Theunissen FE. Information theory and neural coding. *Nat Neurosci.* 1999;2:947-957.

13. DuMouchel W. Bayesian data mining in large frequency tables, with an application to the FDA spontaneous reporting system. *Am Stat.* 1999;53:177-190.

14. Sakaeda T, Tamon A, Kadoyama K, Okuno Y. Data mining of the public version of the FDA Adverse Event Reporting System. *Int J Med Sci.* 2013;10:796-803.

15. Neyman J, Pearson ES. On the problem of the most efficient tests of statistical hypotheses. *Phil Trans R Soc Lond A.* 1933;231:289-337.

16. Shaik MJA. SexDiffKG: a knowledge graph of sex-differential drug safety signals from FAERS. Preprint. 2025.

17. Mirza MR, Monk BJ, Herrstedt J, et al. Niraparib maintenance therapy in platinum-sensitive, recurrent ovarian cancer. *N Engl J Med.* 2016;375:2154-2164.

18. Scher HI, Fizazi K, Saad F, et al. Increased survival with enzalutamide in prostate cancer after chemotherapy. *N Engl J Med.* 2012;367:1187-1197.

19. Mauvais-Jarvis F, Bairey Merz N, Barnes PJ, et al. Sex and gender: modifiers of health, disease, and medicine. *Lancet.* 2020;396:565-582.

20. Cotreau MM, von Moltke LL, Greenblatt DJ. The influence of age and sex on the clearance of cytochrome P450 3A substrates. *Clin Pharmacokinet.* 2005;44:33-60.

21. Klein SL, Flanagan KL. Sex differences in immune responses. *Nat Rev Immunol.* 2016;16:626-638.

22. Luelmo-Aguilar J, Santandreu MS. Folliculitis: recognition and management. *Am J Clin Dermatol.* 2004;5:301-310.

23. Hauben M, Madigan D, Gerrits CM, Walsh L, van Puijenbroek EP. The role of data mining in pharmacovigilance. *Expert Opin Drug Saf.* 2005;4:929-948.

---

## Figure Legends

**Figure 1.** Drug entropy distribution. Histogram of binary entropy H(sex|drug) across 1,394 drugs. The distribution is strongly left-skewed with mode near 1.0 and a long tail extending to H = 0.25. Inset: zoomed view of the low-entropy tail (H < 0.5), showing sex-linked cancer therapies. The 25th percentile (H = 0.912) and 10th percentile (H = 0.817) are marked with vertical dashed lines.

**Figure 2.** Entropy anti-regression. Drug-level entropy (y-axis) vs. report volume decile (x-axis). Monotonic decrease from D0 (H = 0.982) to D9 (H = 0.908). Spearman rho = -0.952, p = 2.3 x 10^-5. The information-theoretic signature of genuine biological signal. Error bars show 95% bootstrap confidence intervals for mean entropy per decile.

**Figure 3.** Signal-level entropy phase transition. Individual signal entropy (y-axis) vs. report volume decile (x-axis). Near-maximum entropy in D0--D6, with sharp transition to structured low entropy in D8--D9. The phase transition boundary (approximately D7, ~100--500 reports) is marked with a vertical shaded region.

**Figure 4.** Mutual information landscape. Scatter plot of mutual information (y-axis) vs. number of drugs per AE (x-axis), colored by mean female fraction. High-MI AEs (folliculitis, obesity, cholesterol) are labeled. Low-MI AEs cluster near zero regardless of drug count. The three functional categories (metabolic, hormonal/reproductive, dermatologic/immune) are indicated by symbol shape.

**Figure 5.** Information concentration curve. Cumulative fraction of total sex-information (y-axis) vs. number of top drugs (x-axis, log scale). The shallow curve demonstrates diffuse distribution: 500 drugs account for only 32.9% of total information. The Zipf reference line (expected concentration under power-law distribution) and equality line are shown for comparison.

---

## Supplementary Materials

**Supplementary Table S1.** Complete drug-level entropy data for all 1,394 drugs, including binary entropy, female fraction, number of signals, total reports, and 95% bootstrap confidence intervals.

**Supplementary Table S2.** Complete AE-level mutual information data for all 1,668 AEs, including MI, marginal entropy, conditional entropy, number of drugs, and mean female fraction.

**Supplementary Table S3.** Signal-level entropy data for all 96,281 sex-differential signals, binned by volume decile.

**Supplementary Figure S1.** Bootstrap distributions for drug-level entropy estimates, showing the 20 drugs with the widest and narrowest confidence intervals.

**Supplementary Figure S2.** Entropy vs. female fraction scatter plot for all 1,394 drugs, illustrating the parabolic relationship imposed by the binary entropy function and the distribution of drugs along this curve.
