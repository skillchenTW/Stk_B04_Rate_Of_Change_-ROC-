**算法交易：Python 編程中的技術指標變化率 (ROC) 實現。**
___
:black_nib:**變化率 (ROC) 是一種技術指標**，用於衡量最近價格與“n”天前價格之間的百分比變化。該指標在零線附近波動，假設我們採用 12 天移動平均線並預測下一個之前的 12 天。眾所周知，交易日基本上是一年的 12 個月，分為 2 部分 6 個月，在“n”天移動平均線的幫助下，我們可以對幾個月進行長期預測考慮。

:black_nib:短期內我們可以使用 2 天移動平均線，其中低於交易則視為賣出，高於交易視為買入。它基本上考慮收盤價和昨天的 12 天或 2 天移動平均線之前關閉並藉助它我們可以分析 2 天后或 12 天后的效果，這基本上乘以顯示結果所需的天數 **ROC 基本上有助於衡量短期勢頭或長期勢頭**。

:black_nib:上升的 ROC 發出看漲信號，而下降的 ROC 發出看跌信號。

:black_nib:計算ROC (Rate Of Change indicators Rate)：

    ROC=[((Close price today - Close price "n" days ago)/Close price "n" days ago))]
    
:black_nib:下面我們將考慮使用正確說明的視頻和 python 代碼來計算變化率 (ROC) 技術指標。

:black_nib:示例代碼：Nifty 的 2 天 ROC

在下面的代碼中，我們使用了 *Series、shift、diff* 和 *join* 函數。

在這裡，我們正在考慮 Series ，它是一個包含數據數組的一維數組對象。在計算的 diff 函數中，我們考慮當前的收盤價，然後我們用“n”天來區分，我們想在之前考慮它以進行預測，該預測用於在移位函數的幫助下獲取。然後我們加入給定的系列使用指定的系列/數據框，最後使用 join 函數進行計算。
___
