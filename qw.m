function tr(M, n, sps)
%M = 4; % Modulation order (alphabet size or number of points in signal constellation)
k = log2(M); % Number of bits per symbol
rng default;
dataIn = randi([0 1],n,1); % Generate vector of binary data
dataSymbolsIn = bit2int(dataIn,k);
dataMod = qammod(dataSymbolsIn,M,'bin'); % Binary-encoded
EbNo = 1;
snr = EbNo+10*log10(k)-10*log10(sps);
receivedSignal = awgn(dataMod,snr,'measured');
sPlotFig = scatterplot(receivedSignal,1,0,'g.');
hold on;
scatterplot(dataMod,1,0,'k*',sPlotFig);