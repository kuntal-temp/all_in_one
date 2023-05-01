# Relational plots

sb.lineplot(x=, y=, data=, hue=)
sb.relplot(x=, y=, hue=, data=, col=, row=)
sb.scatterplot(x=, y=, hue=, data=)


# Distribution plots

sb.histplot(x=, data=, bins=, hue=)
sb.kdeplot(x=, y=, data=, shade=True, cbar=True) [y is optional]
sb.rugplot(x=, data=, height=)


# Categorical plots

sb.catplot(x=, y=, hue=, row=, col= data=, kind=)
sb.barplot(x=, y=, hue=, data=)
sb.violinplot(x=, y=, hue=, data=) [y is optional]
sb.boxplot(x=, y=, hue=, data=) [y is optional]
sb.countplot(x=, hue=, data=)
