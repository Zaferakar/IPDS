import numpy as np



def sinir_agi_softmax(veri, test_verisi):
    test_verisi = np.array(test_verisi)

    # Numericizing class labels
    etiketler = {etiket: idx for idx, etiket in enumerate(set(veri.values()))}
    ters_etiketler = {v: k for k, v in etiketler.items()}

    # Converting data to numpy arrays
    X = np.array(list(veri.keys()))  # vectors
    y = np.array([etiketler[veri[key]] for key in veri.keys()])  # labels

    # Normalize data
    def normalize(veri):
        max_deger = np.max(veri)
        min_deger = np.min(veri)
        return (veri - min_deger) / (max_deger - min_deger)

    X = normalize(X)
    test_verisi = normalize(test_verisi)

    # ReLU activation function
    def relu(x):
        return np.maximum(0, x)
    # Softmax activation function
    def softmax(x):
        x = np.array(x)  # convert inputs to numpy array
        x = x - np.max(x, axis=-1, keepdims=True)
        exp_degerler = np.exp(x)
        toplam = np.sum(exp_degerler, axis=-1, keepdims=True)  # Calculate the total
        return exp_degerler / (toplam + 1e-10)  # Add 1e-10 to avoid division by zero when dividing

    # calculate of Cross-Entropy Loss
    def cross_entropy_loss(cikti, y):
        y_onehot = np.zeros((y.shape[0], len(etiketler)))  # One-hot encoding
        for i in range(y.shape[0]):
            y_onehot[i, y[i]] = 1
        cikti = cikti + 1e-10  # Adding a small constant to prevent division by zero error
        kayip = -np.mean(np.sum(y_onehot * np.log(cikti), axis=1))
        return kayip

    # feedforward
    def ileri_gecis(X, W1, b1, W2, b2):
        z1 = np.dot(X, W1) + b1  # Hidden layer
        a1 = relu(z1)  # ReLU activation
        z2 = np.dot(a1, W2) + b2  # output layer
        cikti = softmax(z2)  # Softmax output
        return cikti, a1

    # backpropagation
    def geri_gecis(X, y, cikti, a1, W1, W2, b1, b2, ogrenme_orani):
        y_onehot = np.zeros((y.shape[0], len(etiketler)))  # One-hot encoding
        for i in range(y.shape[0]):
            y_onehot[i, y[i]] = 1

        # Calculate the error in the output layer
        dcikti = cikti - y_onehot
        dW2 = np.dot(a1.T, dcikti)
        db2 = np.sum(dcikti, axis=0)

        # Calculate the error in the hidden layer
        da1 = np.dot(dcikti, W2.T)
        dz1 = da1 * (a1 > 0)  # Apply ReLU derivative
        dW1 = np.dot(X.T, dz1)
        db1 = np.sum(dz1, axis=0)

        # Update weights
        W1 -= ogrenme_orani * dW1
        b1 -= ogrenme_orani * db1
        W2 -= ogrenme_orani * dW2
        b2 -= ogrenme_orani * db2

        return W1, b1, W2, b2

    # training
    kayip_degeri = []
    def egitim(X, y, epoch_sayisi=1000, ogrenme_orani=0.01):
        girdi_boyutu = X.shape[1]  # Input size
        gizli_boyut = 5  # Hidden layer size
        cikti_boyut = len(etiketler)  # Output size

        # Initialize weights and biases randomly
        W1 = np.random.randn(girdi_boyutu, gizli_boyut)  # First layer weights
        b1 = np.zeros(gizli_boyut)  # Bias of the first layer
        W2 = np.random.randn(gizli_boyut, cikti_boyut)  # Second layer weights
        b2 = np.zeros(cikti_boyut)  # Bias of the second layer

        for epoch in range(epoch_sayisi):
            # Forward pass
            cikti, a1 = ileri_gecis(X, W1, b1, W2, b2)

            # Backward pass
            W1, b1, W2, b2 = geri_gecis(X, y, cikti, a1, W1, W2, b1, b2, ogrenme_orani)

            # calculate of Cross-Entropy Loss
            ce_loss = cross_entropy_loss(cikti, y)

            if epoch % 100 == 0:
                try:
                    kayip_degeri.pop(-1)
                except:
                    pass
                kayip_degeri.append(ce_loss)

        return W1, b1, W2, b2

    # training
    W1, b1, W2, b2 = egitim(X, y, epoch_sayisi=1000, ogrenme_orani=0.01)

    # Making predictions with test data
    def tahmin(test_verisi, W1, b1, W2, b2):
        test_cikti, _ = ileri_gecis(test_verisi.reshape(1, -1), W1, b1, W2, b2)
        tahmin_edilen_sinif_indeksi = np.argmax(test_cikti)
        return ters_etiketler[tahmin_edilen_sinif_indeksi], test_cikti

    tahmin_edilen_sinif, test_cikti = tahmin(test_verisi, W1, b1, W2, b2)

    softmax_sonuc1 = "Softmax Function Estimation Result:         {}".format(tahmin_edilen_sinif)
    softmax_sonuc2 = "MSE:         {}".format(kayip_degeri[0])

    softmax_sonuc = [softmax_sonuc1,softmax_sonuc2,tahmin_edilen_sinif]
    print(softmax_sonuc)
    return softmax_sonuc



def rastgele_orman_regresyonu(giris_verileri,cikis_verileri,tahmin_edilecek_veri):
    def karar_agaci_egit(veri, hedef, maks_derinlik, min_ornek, derinlik=0):
        if len(hedef) < min_ornek or derinlik >= maks_derinlik or np.unique(hedef).size == 1:
            return np.mean(hedef)

        en_iyi_ozellik, en_iyi_esik = en_iyi_bolunme(veri, hedef)
        if en_iyi_ozellik is None:
            return np.mean(hedef)

        sol_indeks = veri[:, en_iyi_ozellik] <= en_iyi_esik
        sag_indeks = veri[:, en_iyi_ozellik] > en_iyi_esik

        sol_agac = karar_agaci_egit(veri[sol_indeks], hedef[sol_indeks], maks_derinlik, min_ornek, derinlik + 1)
        sag_agac = karar_agaci_egit(veri[sag_indeks], hedef[sag_indeks], maks_derinlik, min_ornek, derinlik + 1)

        return {"ozellik": en_iyi_ozellik, "esik": en_iyi_esik, "sol": sol_agac, "sag": sag_agac}

    # Finding the best split point
    def en_iyi_bolunme(veri, hedef):
        en_iyi_ozellik, en_iyi_esik = None, None
        en_iyi_kayip = float("inf")

        for ozellik in range(veri.shape[1]):
            esikler = np.unique(veri[:, ozellik])
            for esik in esikler:
                sol_indeks = veri[:, ozellik] <= esik
                sag_indeks = veri[:, ozellik] > esik

                if len(hedef[sol_indeks]) == 0 or len(hedef[sag_indeks]) == 0:
                    continue

                sol_kayip = np.var(hedef[sol_indeks]) * len(hedef[sol_indeks])
                sag_kayip = np.var(hedef[sag_indeks]) * len(hedef[sag_indeks])
                toplam_kayip = sol_kayip + sag_kayip

                if toplam_kayip < en_iyi_kayip:
                    en_iyi_kayip = toplam_kayip
                    en_iyi_ozellik = ozellik
                    en_iyi_esik = esik

        return en_iyi_ozellik, en_iyi_esik

    # Making predictions in a decision tree
    def karar_agaci_tahmin(veri, agac):
        if not isinstance(agac, dict):
            return agac
        if veri[agac["ozellik"]] <= agac["esik"]:
            return karar_agaci_tahmin(veri, agac["sol"])
        else:
            return karar_agaci_tahmin(veri, agac["sag"])

    # Random Forest Regression Model Training
    def rastgele_orman_egit(veri, hedef, agac_sayisi, maks_derinlik, min_ornek, ozellik_orani):
        orman = []
        for _ in range(agac_sayisi):
            # Random sampling(bootstrap)
            ornek_indeksleri = np.random.choice(len(hedef), len(hedef), replace=True)
            veri_ornek = veri[ornek_indeksleri]
            hedef_ornek = hedef[ornek_indeksleri]

            # Random feature selection
            ozellik_sayisi = veri.shape[1]
            secilen_ozellik_sayisi = max(1, int(ozellik_sayisi * ozellik_orani))
            secilen_ozellikler = np.random.choice(ozellik_sayisi, secilen_ozellik_sayisi, replace=False)
            veri_ornek = veri_ornek[:, secilen_ozellikler]

            # Train the decision tree
            agac = karar_agaci_egit(veri_ornek, hedef_ornek, maks_derinlik, min_ornek)
            orman.append((agac, secilen_ozellikler))

        return orman

    # prediction
    def rastgele_orman_tahmin(veri, orman):
        tahminler = []
        for agac, ozellikler in orman:
            veri_alt = veri[:, ozellikler]
            tahmin = np.array([karar_agaci_tahmin(satir, agac) for satir in veri_alt])
            tahminler.append(tahmin)
        return np.mean(tahminler, axis=0)

    # input data
    giris_verisi = np.array(giris_verileri)
    hedef_degerler = np.array(cikis_verileri)

    # Training the Model
    orman = rastgele_orman_egit(giris_verisi, hedef_degerler, agac_sayisi=10, maks_derinlik=5, min_ornek=2,
                                ozellik_orani=0.6)

    # prediction
    test_verisi = np.array([tahmin_edilecek_veri])
    tahminler = rastgele_orman_tahmin(test_verisi, orman)

    sonuc = ["Regression Estimation Result:         {}".format(tahminler[0]), "", tahminler]


    return sonuc



