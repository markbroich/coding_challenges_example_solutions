# FUNCTIONS

##############################################
# function to look at data frame shape, count NA per column, count and list unique values per column
def df_shape_nacount_unique_countlist(df):
    shape = df.shape 
    print('shape')
    print(shape)
    print('')

    columns = list(df) 
    # count NAs 
    # treat inf as Na
    pd.options.mode.use_inf_as_na = True
    for i in columns:  
        print (i)
        print("Na count")
        print (sum(df[i].isna()))  
        #print("not Na count")
        #print (sum(df_bid_requests[i].notna()))  
        print("")

    # count and list unique values per column
    for i in columns:  
        print (i) 
        print ('unique count') 
        uniq = pd.unique(df[i])
        print(uniq.shape[0])
        print ('unique list') 
        print (uniq)
        print ('') 




##############################################
def plot_time_series(df, col, day=0, hour=0, hour_day=0, plot_kind=0, compare=0, use_xlim=0, use_ylim=0, xmin=0, xmax=1000000, ymin=25000, ymax=28000, z=100, size_x=10, size_y=10, col_bins=24):
    # set fig size
    plt.rcParams["figure.figsize"]=size_x,size_y
    
    # set a color bar with 24 bins for the hours
    twilight_shifted = cm.get_cmap('twilight_shifted', col_bins)
    bar_col= twilight_shifted(range(col_bins))
    # set for hours: blue is increasing light 0 - 12h, red is decreasing light 13-24h 
    #
    # use axis limits
    axes = plt.gca()
    if(use_xlim==1):
        axes.set_xlim([xmin,xmax])
    if(use_ylim==1):
        axes.set_ylim([ymin,ymax])
    #    
    # format x axis as time
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    #plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    #

    # set fig size
    plt.rcParams["figure.figsize"]=size_x,size_y
    
    # set a color bar with 24 bins for the hours
    twilight_shifted = cm.get_cmap('twilight_shifted', col_bins)
    bar_col= twilight_shifted(range(col_bins))
    # set for hours: blue is increasing light 0 - 12h, red is decreasing light 13-24h 
    #
    # use axis limits
    axes = plt.gca()
    if(use_xlim==1):
        axes.set_xlim([xmin,xmax])
    if(use_ylim==1):
        axes.set_ylim([ymin,ymax])
    #    
    # format x axis as time
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    #plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    #
    if(day==1):
        # by day
        if(plot_kind==0):
            if(compare==0):
                df[col].groupby(df["date_time"].dt.day).count().plot()
            elif(compare==1):
                df[col].groupby(df["date_time"].dt.day).sum().plot() 
            else:
                df[col].groupby(df["date_time"].dt.day).count().plot()
                df[col].groupby(df["date_time"].dt.day).sum().plot() 
        else:
            df[col].groupby(df["date_time"].dt.day).count().plot(kind="bar", color = bar_col)
    if(hour==1):
        # by hour
        if(plot_kind==0):
            if(compare==0):
                df[col].groupby(df_bid_requests["date_time"].dt.hour).count().plot()
            elif(compare==1):
                df[col].groupby(df_bid_requests["date_time"].dt.hour).sum().plot()
            else:
                df[col].groupby(df_bid_requests["date_time"].dt.hour).count().plot()
                df[col].groupby(df_bid_requests["date_time"].dt.hour).sum().plot() 
        else:
            df[col].groupby(df["date_time"].dt.hour).count().plot(kind="bar", color = bar_col)
    if(hour_day==1):
        if(plot_kind==0):
            if(compare==0):
                df[col].groupby([df_bid_requests["date_time"].dt.day, df_bid_requests["date_time"].dt.hour]).count().plot()
            elif(compare==1):
                df[col].groupby([df_bid_requests["date_time"].dt.day, df_bid_requests["date_time"].dt.hour]).sum().plot()
            else:
                df[col].groupby([df_bid_requests["date_time"].dt.day, df_bid_requests["date_time"].dt.hour]).count().plot()
                df[col].groupby([df_bid_requests["date_time"].dt.day, df_bid_requests["date_time"].dt.hour]).sum().plot()      
        else:
            df[col].groupby([df_bid_requests["date_time"].dt.day, df_bid_requests["date_time"].dt.hour]).count().plot(kind="bar", color = bar_col)



##############################################
# function to plot attrubutes independent of time, or per day or per hour
def plot_attribute_bars(df, test=0, no_time=0, day=0, hour=0):
    plt.rcParams["figure.figsize"]=5,5
    if(no_time==1):
        ## independent of time
        df[['age']].apply(pd.value_counts).plot(kind='bar', subplots=True)
        df[['location']].apply(pd.value_counts).plot(kind='bar', subplots=True)
        df[['gender']].apply(pd.value_counts).plot(kind='bar', subplots=True)
        if(test==1):
            df[['test']].apply(pd.value_counts).plot(kind='bar', subplots=True)
    if(day==1):    
        # by day
        by_time = pd.DataFrame(df["date_time"].dt.day)
        counts = by_time.apply(pd.value_counts) 
        counts['val'] = list(counts.index) 
        counts = counts.sort_values(by=['val'])
        counts['date_time'].plot(kind='bar', subplots=True)
    if(hour==1):
        # by hour
        by_time = pd.DataFrame(df["date_time"].dt.hour)
        counts = by_time.apply(pd.value_counts)
        counts['val'] = list(counts.index) 
        counts = counts.sort_values(by=['val'])
        counts['date_time'].plot(kind='bar', subplots=True)



##############################################
# function to subsample the states
def subsample_state(df):
    temp = df[df['location']=='NC']
    temp__=temp.sample(n=NC_sample_n, random_state=1)

    temp = df[df['location']=='FL']
    temp_=temp.sample(n=FL_sample_n, random_state=1)
    temp__ = temp__.append(temp_)
    temp = df[df['location']=='GA']
    temp_=temp.sample(n=GA_sample_n, random_state=1)
    temp__ = temp__.append(temp_)
    temp = df[df['location']=='VA']
    temp_=temp.sample(n=VA_sample_n, random_state=1)
    temp__ = temp__.append(temp_)
    temp = df[df['location']=='TN']
    temp_=temp.sample(n=TN_sample_n, random_state=1)
    temp__ = temp__.append(temp_)
    temp = df[df['location']=='SC']
    temp_=temp.sample(n=SC_sample_n, random_state=1)
    temp__ = temp__.append(temp_)
    temp = df[df['location']=='AL']
    temp_=temp.sample(n=AL_sample_n, random_state=1)
    temp__ = temp__.append(temp_)
    temp = df[df['location']=='KY']
    temp_=temp.sample(n=KY_sample_n, random_state=1)
    temp__ = temp__.append(temp_)
    temp = df[df['location']=='MS']
    temp_=temp.sample(n=MS_sample_n, random_state=1)
    temp__ = temp__.append(temp_)
    temp = df[df['location']=='AR']
    temp_=temp.sample(n=AR_sample_n, random_state=1)
    temp__ = temp__.append(temp_)
    temp = df[df['location']=='LA']
    temp_=temp.sample(n=LA_sample_n, random_state=1)
    temp__ = temp__.append(temp_)
    df_resamp = temp__
    
    return(df_resamp)



##############################################
# AB test-specific_functions 1:
# as per https://towardsdatascience.com/the-math-behind-a-b-testing-with-example-code-part-1-of-2-7be752e1d06f
def pooled_prob(N_A, N_B, X_A, X_B):
    """Returns pooled probability for two samples"""
    return (X_A + X_B) / (N_A + N_B)


def pooled_SE(N_A, N_B, X_A, X_B):
    """Returns the pooled standard error for two samples"""
    p_hat = pooled_prob(N_A, N_B, X_A, X_B)
    SE = np.sqrt(p_hat * (1 - p_hat) * (1 / N_A + 1 / N_B))
    return SE


def confidence_interval(sample_mean=0, sample_std=1, sample_size=1,
                        sig_level=0.05):
    """Returns the confidence interval as a tuple"""
    z = z_val(sig_level)

    left = sample_mean - z * sample_std / np.sqrt(sample_size)
    right = sample_mean + z * sample_std / np.sqrt(sample_size)

    return (left, right)


def z_val(sig_level=0.05, two_tailed=True):
    """Returns the z value for a given significance level"""
    z_dist = scs.norm()
    if two_tailed:
        sig_level = sig_level/2
        area = 1 - sig_level
    else:
        area = 1 - sig_level

    z = z_dist.ppf(area)

    return z


def ab_dist(stderr, d_hat=0, group_type='control'):
    """Returns a distribution object depending on group type
    Examples:
    Parameters:
        stderr (float): pooled standard error of two independent samples
        d_hat (float): the mean difference between two independent samples
        group_type (string): 'control' and 'test' are supported
    Returns:
        dist (scipy.stats distribution object)
    """
    if group_type == 'control':
        sample_mean = 0

    elif group_type == 'test':
        sample_mean = d_hat

    # create a normal distribution which is dependent on mean and std dev
    dist = scs.norm(sample_mean, stderr)
    return dist


def min_sample_size(bcr, mde, power=0.8, sig_level=0.05):
    """Returns the minimum sample size to set up a split test
    Arguments:
        bcr (float): probability of success for control, sometimes
        referred to as baseline conversion rate
        mde (float): minimum change in measurement between control
        group and test group if alternative hypothesis is true, sometimes
        referred to as minimum detectable effect
        power (float): probability of rejecting the null hypothesis when the
        null hypothesis is false, typically 0.8
        sig_level (float): significance level often denoted as alpha,
        typically 0.05
    Returns:
        min_N: minimum sample size (float)
    References:
        Stanford lecture on sample sizes
        http://statweb.stanford.edu/~susan/courses/s141/hopower.pdf
    """
    # standard normal distribution to determine z-values
    standard_norm = scs.norm(0, 1)

    # find Z_beta from desired power
    Z_beta = standard_norm.ppf(power)

    # find Z_alpha
    Z_alpha = standard_norm.ppf(1-sig_level/2)

    # average of probabilities from both groups
    pooled_prob = (bcr + bcr+mde) / 2

    min_N = (2 * pooled_prob * (1 - pooled_prob) * (Z_beta + Z_alpha)**2
             / mde**2)

    return min_N


def p_val(N_A, N_B, p_A, p_B):
    """Returns the p-value for an A/B test"""
    return scs.binom(N_A, p_A).pmf(p_B * N_B)



##############################################
# AB test-specific_functions 2:
# as per https://towardsdatascience.com/the-math-behind-a-b-testing-with-example-code-part-1-of-2-7be752e1d06f


def plot_norm_dist(ax, mu, sig, with_CI=False, sig_level=0.05, label=None):
    """Adds a normal distribution to the axes provided
    Example:
        plot_norm_dist(ax, 0, 1)  # plots a standard normal distribution
    Parameters:
        ax (matplotlib axes)
        mu (float): mean of the normal distribution
        sig (float): standard deviation of the normal distribution
    Returns:
        None: the function adds a plot to the axes object provided
    """
    x = np.linspace(mu - 12 * sig, mu + 12 * sig, 1000)
    y = scs.norm(mu, sig).pdf(x)
    ax.plot(x, y, label=label)

    if with_CI:
        plot_CI(ax, mu, sig, sig_level=sig_level)

        
def plot_CI(ax, mu, s, sig_level=0.05, color='grey'):
    """Calculates the two-tailed confidence interval and adds the plot to
    an axes object.
    Example:
        plot_CI(ax, mu=0, s=stderr, sig_level=0.05)
    Parameters:
        ax (matplotlib axes)
        mu (float): mean
        s (float): standard deviation
    Returns:
        None: the function adds a plot to the axes object provided
    """
    # z = scs.norm().ppf(1 - sig_level/2)
    # left = mu - z * s
    # right = mu + z * s
    left, right = confidence_interval(sample_mean=mu, sample_std=s,
                                      sig_level=sig_level)
    ax.axvline(left, c=color, linestyle='--', alpha=0.5)
    ax.axvline(right, c=color, linestyle='--', alpha=0.5)


def plot_null(ax, stderr):
    """Plots the null hypothesis distribution where if there is no real change,
    the distribution of the differences between the test and the control groups
    will be normally distributed.
    The confidence band is also plotted.
    Example:
        plot_null(ax, stderr)
    Parameters:
        ax (matplotlib axes)
        stderr (float): the pooled standard error of the control and test group
    Returns:
        None: the function adds a plot to the axes object provided
    """
    plot_norm_dist(ax, 0, stderr, label="Null")
    plot_CI(ax, mu=0, s=stderr, sig_level=0.05)


def plot_alt(ax, stderr, d_hat):
    """Plots the alternative hypothesis distribution where if there is a real
    change, the distribution of the differences between the test and the
    control groups will be normally distributed and centered around d_hat
    The confidence band is also plotted.
    Example:
        plot_alt(ax, stderr, d_hat=0.025)
    Parameters:
        ax (matplotlib axes)
        stderr (float): the pooled standard error of the control and test group
    Returns:
        None: the function adds a plot to the axes object provided
    """
    plot_norm_dist(ax, d_hat, stderr, label="Alternative")
    plot_CI(ax, mu=d_hat, s=stderr, sig_level=0.05)


def abplot(N_A, N_B, bcr, d_hat, sig_level=0.05, show_power=False,
           show_alpha=False, show_beta=False, show_p_value=False,
           show_legend=True):
    """Example plot of AB test
    Example:
        abplot(n=4000, bcr=0.11, d_hat=0.03)
    Parameters:
        n (int): total sample size for both control and test groups (N_A + N_B)
        bcr (float): base conversion rate; conversion rate of control
        d_hat: difference in conversion rate between the control and test
            groups, sometimes referred to as **minimal detectable effect** when
            calculating minimum sample size or **lift** when discussing
            positive improvement desired from launching a change.
    Returns:
        None: the function plots an AB test as two distributions for
        visualization purposes
    """
    # create a plot object
    fig, ax = plt.subplots(figsize=(12, 6))

    # define parameters to find pooled standard error
    X_A = bcr * N_A
    X_B = (bcr + d_hat) * N_B
    stderr = pooled_SE(N_A, N_B, X_A, X_B)

    # plot the distribution of the null and alternative hypothesis
    plot_null(ax, stderr)
    plot_alt(ax, stderr, d_hat)

    # set extent of plot area
    ax.set_xlim(-3 * d_hat, 3 * d_hat)

    # shade areas according to user input
    if show_power:
        show_area(ax, d_hat, stderr, sig_level, area_type='power')
    if show_alpha:
        show_area(ax, d_hat, stderr, sig_level, area_type='alpha')
    if show_beta:
        show_area(ax, d_hat, stderr, sig_level, area_type='beta')

    # show p_value based on the binomial distributions for the two groups
    if show_p_value:
        null = ab_dist(stderr, 'control')
        p_val = p_value(N_A, N_B, bcr, bcr+d_hat)
        ax.text(3 * stderr, null.pdf(0),
                'p-value = {0:.3f}'.format(p_val),
                fontsize=12, ha='left')

    # option to show legend
    if show_legend:
        plt.legend()

    plt.xlabel('d')
    plt.ylabel('PDF')
    plt.show()


def show_area(ax, d_hat, stderr, sig_level, area_type='power'):
    """Fill between upper significance boundary and distribution for
    alternative hypothesis
    """
    left, right = confidence_interval(sample_mean=0, sample_std=stderr,
                                      sig_level=sig_level)
    x = np.linspace(-12 * stderr, 12 * stderr, 1000)
    null = ab_dist(stderr, 'control')
    alternative = ab_dist(stderr, d_hat, 'test')

    # if area_type is power
    # Fill between upper significance boundary and distribution for alternative
    # hypothesis
    if area_type == 'power':
        ax.fill_between(x, 0, alternative.pdf(x), color='green', alpha='0.25',
                        where=(x > right))
        ax.text(-3 * stderr, null.pdf(0),
                'power = {0:.3f}'.format(1 - alternative.cdf(right)),
                fontsize=12, ha='right', color='k')

    # if area_type is alpha
    # Fill between upper significance boundary and distribution for null
    # hypothesis
    if area_type == 'alpha':
        ax.fill_between(x, 0, null.pdf(x), color='green', alpha='0.25',
                        where=(x > right))
        ax.text(-3 * stderr, null.pdf(0),
                'alpha = {0:.3f}'.format(1 - null.cdf(right)),
                fontsize=12, ha='right', color='k')

    # if area_type is beta
    # Fill between distribution for alternative hypothesis and upper
    # significance boundary
    if area_type == 'beta':
        ax.fill_between(x, 0, alternative.pdf(x), color='green', alpha='0.25',
                        where=(x < right))
        ax.text(-3 * stderr, null.pdf(0),
                'beta = {0:.3f}'.format(alternative.cdf(right)),
                fontsize=12, ha='right', color='k')



##############################################
# AB test-specific_functions 3:
# From "AB Testing With Python - Walkthrough Udacity's Course Final Project" By Tammy Rotem

# From "AB Testing With Python - Walkthrough Udacity's Course Final Project" By Tammy Rotem
#Get standard deviations 1 & 2, that is for both the baseline and for expected changed rate 

#Inputs: required alpha value (alpha should already fit the required test)
#Returns: z-score for given alpha
def get_z_score(alpha):
    return norm.ppf(alpha)

# Inputs p-baseline conversion rate which is our estimated p and d-minimum detectable change
# Returns
def get_sds(p,d):
    sd1=mt.sqrt(2*p*(1-p))
    sd2=mt.sqrt(p*(1-p)+(p+d)*(1-(p+d)))
    sds=[sd1,sd2]
    return sds

# Inputs:sd1-sd for the baseline,sd2-sd for the expected change,alpha,beta,d-d_min,p-baseline estimate p
# Returns: the minimum sample size required per group according to metric denominator
def get_sampSize(sds,alpha,beta,d):
    n=pow((get_z_score(1-alpha/2)*sds[0]+get_z_score(1-beta)*sds[1]),2)/pow(d,2)
    return n


