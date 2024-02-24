### Результати тестування:

**Array size: 100**
- Insertion sort time: 0.000134 seconds
- Merge sort time: 0.000108 seconds
- Timsort (sorted) time: 0.000006 seconds
- Timsort (sort) time: 0.000003 seconds

**Array size: 1000**
- Insertion sort time: 0.014467 seconds
- Merge sort time: 0.001419 seconds
- Timsort (sorted) time: 0.000061 seconds
- Timsort (sort) time: 0.000044 seconds

**Array size: 10000**
- Insertion sort time: 1.512929 seconds
- Merge sort time: 0.017545 seconds
- Timsort (sorted) time: 0.000768 seconds
- Timsort (sort) time: 0.000707 seconds

### Висновки:

1. **Timsort** (як `sorted`, так і метод `sort`) є значно швидшим за сортування злиттям та сортування вставками на всіх розмірах масивів. Це підтверджує ефективність гібридного підходу Timsort, який поєднує в собі переваги сортування злиттям та сортування вставками.

2. **Сортування вставками** (Insertion sort) показує найгірші результати, особливо на великих масивах, що відповідає його теоретичній складності O(n²).

3. **Сортування злиттям** (Merge sort) є значно швидшим за сортування вставками та має більш стабільну продуктивність, але все ж поступається Timsort.

4. Різниця між `sorted` та методом `sort` є незначною, але метод `sort` зазвичай трохи швидший, оскільки він сортує масив на місці, без створення додаткової копії.

Ці результати підкреслюють, чому Timsort є вибором за замовчуванням для сортування в Python та є набагато ефективнішим для більшості випадків, ніж інші алгоритми сортування.
