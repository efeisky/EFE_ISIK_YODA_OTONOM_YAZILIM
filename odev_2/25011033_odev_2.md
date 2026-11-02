## Git ve GitHub Hakkında Kavramlar

**Repository**, sözlükte depo, dolap anlamına gelen. GitHub üzerinde ise saklanmak istenen dosyaların projesel bazda ayrıldığı saklama alanlarıdır. Kodda kimin, ne zaman ve hangi değişiklikleri yaptığının kaydını tutar ve projelerin geçmiş sürümlerinin de saklandığı dijital kayıt alanlarıdır.

**Commit**, seçilmiş repository içerisindeki dosyaların anlık kaydını dijital ortama atılmasını sağlayan işlemdir. ``git commit -m "First Commit" `` komutunu terminalde kullanarak çalışabilmektedir. Dosya değişikliğine dair kimin ne zaman yaptığını belirten kayıt tutar.

**Branch**, projenin anlık olarak kullanılan versiyonunun yanında aynı repository içerisinde farklı bir dal açarak deneme ve yeni özellik ekleme sürecinde kolaylık sunar. Birden çok branch kurularak paralel olarak çalışma sağlanabilir.

**Stage**, kod bloklarındaki değişikliğin commit işlemi öncesi seçilip bir araya getirildiği ara aşamadır. ``git add . ``, `` git add command.rs `` gibi komutlar ile bu işlem gerçekleştirilir.

**Merge**, farklı branchlarda gerçekleştirilen kod değişikliklerinin tek bir branch üzerinde birleştirilme işlemine denir. Bu sayede farklı özellikler üzerinde çalışan kişiler bu yeni featureları tek seferde kodun içine dahil edebilirler.

**Pull**, GitHub’da bir repository içerisinde bulunan kodları kendi bilgisayarımıza çekmemizi ve otomatik olarak branch birleştirmeyi sağlayan Git komutudur. ``git pull origin main``, ``git fetch`` ve ``git merge`` komutlarının birleşimi olarak çalışır.

**Push**, bilgisayarımızda aktif projede yaptığımız commit edilen değişiklikleri GitHub’a aktarma işlemini yapar. ``git push origin main`` olarak kullanılabilir.

## Takımlar Neden Git ve GitHub Kullanır
* Takımlar, birden fazla kişiden oluştukları ve herkesin kendi bilgisayarı üzerinde farklı çalışmalar yaptığı için daha sonradan tüm bilgisayarlardaki kodların toplanması zor olacağından dolayı ortak bir depo olan GitHub’ı kullanmaktadırlar. 
* Tüm kodlar yedeklenmiş şekilde bir serverda bulunur bu sayede güvendedir.
* Kimin hangi kodu ne zaman değiştirdiği açıkça görülebilir bu yüzden karmaşanın önüne geçilir.
* Bir kişi yeni bir feature hazırladığı zaman diğer ekip üyeleri de görebilir ve gerekli test işlemlerini yapabilir.

### Versiyon Kontrolüne Neden İhtiyaç Duyulur?
* Versiyon kontrolü, kişi sayısı arttıkça herkesin farklı kodlar yazmasıyla oluşan karmaşanın önüne geçmek için elzemdir. 
* Bu sistemlere Versiyon Kontrol Sistemi(VCS) denir. Bu sistemler sayesinde tek bir dosya için o dosyaya ait tüm log geçmişi saklanır ve gerektiğinde versiyonlar arası geçiş yapılabilir.
* VCS sistemleri sayesinde hataların izlenebilirliği ve yazılımın gelişim hızı oldukça kolaylaşır ve hızlanır.
### Git ile GitHub arasındaki fark nedir?
Git, bilgisayar üzerine kurulan ve yazılan kodun geçmiş kayıtlarını yerel olarak takip edebileceğimiz bir VCS sistemidir. Açık kaynaklı bir terminal aracıdır.

GitHub, Git depolarının dünya üzerinde farklı sunucularda saklanması sayesinde oluşan bulut tabanlı bir platformdur. İnternet üzerinden erişilebilir. Aynı zamanda Git ile terminal üzerinden dosya işlemleri yapılabilir.

### Ekip çalışmasına katkıları nedir?
GitHub’ın ekip çalışmasına temelde katkısı, birden fazla geliştiricinin paralel olarak aynı proje üzerinde herhangi bir karışıklık olmadan çalışabilmesidir.

Her ekip üyesinin proje üzerinde yaptığı değişiklikler izlenebildiği ve herhangi bir yerde oluşan hatanın çok kolay bir şekilde eski versiyonuna alınabilmesi sayesinde tercih edilebilir.

Bunların dışında repositoryde farklı dalların bulunması ile ana koda zarar vermeden yeni özellikler test edilebilir ve geliştirilebilir. Daha sonrasında merge işlemi yapılarak hızlıca ve güvenli bir şekilde ana koda etkide bulunulabilir.

### GitHub'ın Proje Yönetim Özellikleri
GitHub’ın proje yönetim özellikleri olarak şunlar örnek verilebilir. 
+ Issues kısmı, projede yapılması gereken işlerin, geliştirmeleri önerilerinin ve hataların yazıldığı bölümdür. 
+ Milestone kısmı, projenin ne kadar zamanda ne kadar yol alması gerektiğine dair yol haritası kısmıdır.
+ Actions, test, derleme ve dağıtım işlerinin otomatik olarak yapılmasını sağlar.
+ Discussions kısmı, ekip üyelerinin projeye dair tartışmalarını yapabildikleri kısımdır.

### Kulüp ve Takım İçin Önemi
Kulüp ve takım için önemi ödevde bir çok yerde bahsedildiği için tekrardan bahsetmeye gerek duymuyorum ancak kısa bir şekilde özetlemek gerekirse, projenin düzenli, bulutta yedekli, takip edilebilir ve karmaşıklık çıkmadan yapılması için kritik bir uygulamadır.

### Otonom Araç Projesindeki Yeri
Otonom araç sistemlerinde birçok sensör ve yapay zeka bulunur. Bu sensörlerin ve yapay zekaların eş zamanlı olarak üzerinde çalışması için ve bu çalışma sırasında da ana projeye zarar vermeden güvenilir biçimde yapmak için oldukça önemlidir. Her ekip üyesi kendi bölümünü farklı branchlerde geliştirebilir ve o şekilde ana koda dahil edebilir.
### Dikkat Edilmesi Gerekenler
* Değişiklikler ana branch'e eklenmeden önce test edilmelidir.
* Yeni özellikler geliştirilirken ayrı branch'ler kullanılmalıdır.
* Eğer API anahtarı gerektirecek bir kod yazılıyorsa .env dosyalarında saklanmalı ve Github’da gözüktürülmemelidir.
* Gizli bilgi içeren veya Github’a yüklenmesi gerekmeyen dosyalar .gitignore aracılığıyla hariç bırakılmalıdır.

