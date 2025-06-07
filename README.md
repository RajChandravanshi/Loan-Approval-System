\documentclass{article}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{geometry}
\geometry{margin=1in}

\title{Loan Approval Classification Project Report}
\author{Raj Chandravanshi}
\date{}

\begin{document}

\maketitle

\section*{Objective}
To predict the likelihood of loan approval using demographic, financial, and credit history features via various machine learning and deep learning models.

\section*{Dataset Overview}
\begin{itemize}
    \item \textbf{Rows}: 45,000
    \item \textbf{Columns}: 14
    \item \textbf{Target Variable}: \texttt{loan\_status}
\end{itemize}

\subsection*{Features}
\begin{itemize}
    \item Demographics: \texttt{person\_age}, \texttt{person\_gender}, \texttt{person\_education}
    \item Financial: \texttt{person\_income}, \texttt{loan\_amnt}, \texttt{loan\_percent\_income}, \texttt{credit\_score}
    \item Employment: \texttt{person\_emp\_exp}
    \item Credit History: \texttt{cb\_person\_cred\_hist\_length}, \texttt{previous\_loan\_defaults\_on\_file}
    \item Loan Info: \texttt{loan\_intent}, \texttt{loan\_int\_rate}, \texttt{person\_home\_ownership}
\end{itemize}

\section*{Data Cleaning}
\begin{itemize}
    \item No missing or duplicate values.
    \item Detected 15,438 outliers (not removed to retain label integrity).
\end{itemize}

\section*{Exploratory Data Analysis (EDA)}
\subsection*{Categorical Variables}
Count plots were generated to assess loan approval distribution across categorical features.

\subsection*{Numerical Variables}
Used histograms, KDEs, box plots:
\begin{itemize}
    \item Observed skewness in \texttt{person\_income}, \texttt{loan\_int\_rate}
    \item Strong impact from \texttt{credit\_score}, \texttt{loan\_amnt}
\end{itemize}

\subsection*{Correlation}
A heatmap showed that \texttt{credit\_score} and \texttt{loan\_int\_rate} are highly influential.

\section*{Feature Engineering}
\begin{itemize}
    \item One-hot encoding for categorical features.
    \item Used \texttt{ColumnTransformer}.
    \item Train-test split: 80/20.
\end{itemize}

\section*{Modeling (Before SMOTE)}
\subsection*{Models Used}
\begin{itemize}
    \item Decision Tree, Random Forest, Extra Trees, XGBoost, Gradient Boosting
\end{itemize}

\begin{table}[h]
\centering
\begin{tabular}{lcccc}
\toprule
\textbf{Model} & \textbf{Accuracy} & \textbf{Precision} & \textbf{Recall} & \textbf{ROC AUC} \\
\midrule
Decision Tree & 0.8991 & 0.7707 & 0.7766 & 0.8553 \\
Random Forest & 0.9264 & 0.8919 & 0.7607 & 0.9731 \\
Extra Trees   & 0.9152 & 0.8537 & 0.7458 & 0.9660 \\
XGBoost       & \textbf{0.9324} & \textbf{0.8822} & \textbf{0.8026} & \textbf{0.9774} \\
Gradient Boosting & 0.9233 & 0.8765 & 0.7621 & 0.9717 \\
\bottomrule
\end{tabular}
\caption{Model Performance Before SMOTE}
\end{table}

\section*{Class Imbalance Handling (SMOTE)}
\begin{itemize}
    \item SMOTE applied to balance classes.
    \item Dataset expanded to 70,000 samples.
\end{itemize}

\subsection*{Post-SMOTE Results}

\begin{table}[h]
\centering
\begin{tabular}{lcccc}
\toprule
\textbf{Model} & \textbf{Accuracy} & \textbf{Precision} & \textbf{Recall} & \textbf{ROC AUC} \\
\midrule
Decision Tree & 0.9270 & 0.9258 & 0.9286 & 0.9270 \\
Random Forest & 0.9524 & 0.9601 & 0.9441 & 0.9922 \\
Extra Trees   & 0.9492 & 0.9522 & 0.9460 & 0.9916 \\
XGBoost       & \textbf{0.9563} & \textbf{0.9648} & \textbf{0.9472} & \textbf{0.9936} \\
Gradient Boosting & 0.9439 & 0.9440 & 0.9439 & 0.9900 \\
\bottomrule
\end{tabular}
\caption{Model Performance After SMOTE}
\end{table}

\section*{Deep Learning Models}

\subsection*{PyTorch-based ANN}
\begin{itemize}
    \item 2 hidden layers with ReLU, BatchNorm, Dropout
    \item Optimizer: Adam, Loss: BCEWithLogitsLoss
    \item Trained for 20 epochs, batch size = 256
    \item Performance was suboptimal
\end{itemize}

\subsection*{Keras-based ANN}
\begin{itemize}
    \item 4 hidden layers with ReLU, BatchNorm, Dropout
    \item Optimizer: Adam, Loss: Binary Crossentropy
    \item Trained for 100 epochs with validation
    \item Recall varied widely (from 0.3 to 0.99), indicating instability
\end{itemize}

\section*{Conclusions}
\begin{itemize}
    \item \textbf{Best Model:} XGBoost (after SMOTE)
    \item \textbf{Best Metric:} ROC AUC = 0.9936
    \item \textbf{Important Features:} \texttt{credit\_score}, \texttt{loan\_amnt}, \texttt{loan\_int\_rate}
    \item \textbf{Recommendation:} Use tree-based ensemble models like XGBoost for production
\end{itemize}

\end{document}
