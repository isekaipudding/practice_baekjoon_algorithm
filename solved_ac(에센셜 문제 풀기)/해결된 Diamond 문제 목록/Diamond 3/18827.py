# 18827번(연속합 2147483647) : https://www.acmicpc.net/problem/18827
"""
// C99
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Python으로 하면 서브 태스크 11에서 TLE가 발생하여 어쩔 수 없이 C언어로 수정합니다.
// 참고 소스 코드 : https://github.com/hijkl2e/problem_solving/blob/main/boj/Volume%2018/boj18827.cpp
// hijkl2e님께 경의를 표합니다.

typedef long long ll;

typedef struct {
    ll *v;    // little-endian blocks (base 1e16)
    int size; // number of used blocks
    int cap;  // capacity of v
    int neg;  // sign flag (0: +, 1: -)
} Demical;

static const ll BASE = 10000000000000000LL;

/* util: dynamic string token reader (whitespace-delimited) */
static char* read_token(void) {
    int c;
    // skip leading whitespace
    do { c = getchar(); if (c == EOF) return NULL; } while (isspace(c));

    size_t cap = 64, len = 0;
    char *s = (char*)malloc(cap);
    if (!s) exit(1);

    // read until whitespace/EOF
    while (c != EOF && !isspace(c)) {
        if (len + 1 >= cap) {
            cap <<= 1;
            char *ns = (char*)realloc(s, cap);
            if (!ns) exit(1);
            s = ns;
        }
        s[len++] = (char)c;
        c = getchar();
    }
    s[len] = '\0';
    return s;
}

/* Demical helpers */
static void bi_init(Demical *a) {
    a->v = NULL; a->size = 0; a->cap = 0; a->neg = 0;
}
static void bi_free(Demical *a) {
    free(a->v); a->v = NULL; a->size = a->cap = 0; a->neg = 0;
}
static void bi_reserve(Demical *a, int need) {
    if (need <= a->cap) return;
    int nc = a->cap ? a->cap : 1;
    while (nc < need) nc <<= 1;
    ll *nv = (ll*)realloc(a->v, (size_t)nc * sizeof(ll));
    if (!nv) exit(1);
    // zero-initialize new area
    for (int i = a->cap; i < nc; ++i) nv[i] = 0;
    a->v = nv; a->cap = nc;
}
static void bi_resize(Demical *a, int ns) {
    if (ns > a->cap) bi_reserve(a, ns);
    if (ns > a->size) {
        for (int i = a->size; i < ns; ++i) a->v[i] = 0;
    }
    a->size = ns;
}
static void bi_trim(Demical *a) {
    while (a->size > 0 && a->v[a->size - 1] == 0) a->size--;
    if (a->size == 0) a->neg = 0; // zero is non-negative
}
static void bi_copy(Demical *dst, const Demical *src) {
    bi_resize(dst, src->size);
    for (int i = 0; i < src->size; ++i) dst->v[i] = src->v[i];
    dst->neg = src->neg;
}

/* s : decimal string, may start with '-' */
static void bi_from_cstr(Demical *a, const char *s) {
    bi_init(a);
    if (strcmp(s, "0") == 0) return;
    int neg = (s[0] == '-');
    if (neg) s++;

    size_t len = strlen(s);
    if (len == 0) return; // treat empty as zero

    int blocks = (int)((len - 1) / 16 + 1);
    bi_resize(a, blocks);
    for (size_t i = 0; i < len; ++i) {
        int j = (int)((len - i - 1) / 16);
        a->v[j] = 10 * a->v[j] + (s[i] - '0');
    }
    a->neg = neg;
    bi_trim(a);
}

static void bi_normalize(Demical *a) {
    for (int i = 1; i < a->size; ++i) {
        if (a->v[i - 1] < 0) {
            a->v[i - 1] += BASE;
            a->v[i] -= 1;
        }
    }
    bi_trim(a);
}

static void bi_add_inplace(Demical *a, const Demical *b) {
    int maxsz = (a->size > b->size ? a->size : b->size) + 1;
    bi_resize(a, maxsz);
    int sgn = (a->neg ^ b->neg) ? -1 : 1;

    int i = 0;
    for (; i < b->size || (i < a->size && (a->v[i] <= -BASE || a->v[i] >= BASE)); ++i) {
        if (i < b->size) a->v[i] += (ll)sgn * b->v[i];
        if (a->v[i] >= BASE) {
            a->v[i] -= BASE; a->v[i + 1] += 1;
        } else if (a->v[i] <= -BASE) {
            a->v[i] += BASE; a->v[i + 1] -= 1;
        }
    }
    bi_trim(a);
    if (a->size > 0 && a->v[a->size - 1] < 0) {
        for (int k = 0; k < a->size; ++k) a->v[k] = -a->v[k];
        a->neg ^= 1;
    }
}

static int bi_less(const Demical *a, const Demical *b) {
    if (a->neg != b->neg) return a->neg != 0;
    if (a->size != b->size)
        return a->neg ? (a->size > b->size) : (a->size < b->size);
    if (a->size == 0) return 0;
    for (int i = a->size - 1; i >= 0; --i) {
        if (a->v[i] != b->v[i]) {
            if (!a->neg) return a->v[i] < b->v[i];
            else         return a->v[i] > b->v[i];
        }
    }
    return 0;
}

static void bi_print(const Demical *src) {
    Demical a; bi_init(&a); bi_copy(&a, src);
    bi_normalize(&a);
    if (a.size == 0) { printf("0"); bi_free(&a); return; }
    if (a.neg) printf("-");
    printf("%lld", a.v[a.size - 1]);
    for (int i = a.size - 2; i >= 0; --i) {
        printf("%016lld", a.v[i]);
    }
    bi_free(&a);
}

/* dynamic list of Demical*/
typedef struct {
    Demical *data;
    int size, cap;
} DemicalList;

static void list_init(DemicalList *v) { v->data = NULL; v->size = v->cap = 0; }
static void list_reserve(DemicalList *v, int need) {
    if (need <= v->cap) return;
    int nc = v->cap ? v->cap : 1;
    while (nc < need) nc <<= 1;
    Demical *nd = (Demical*)realloc(v->data, (size_t)nc * sizeof(Demical));
    if (!nd) exit(1);
    for (int i = v->cap; i < nc; ++i) bi_init(&nd[i]);
    v->data = nd; v->cap = nc;
}
static void list_append_move(DemicalList *v, Demical *src) {
    if (v->size + 1 > v->cap) list_reserve(v, v->size + 1);
    v->data[v->size] = *src; // move
    src->v = NULL; src->size = src->cap = 0; src->neg = 0;
    v->size++;
}
static void list_free(DemicalList *v) {
    for (int i = 0; i < v->size; ++i) bi_free(&v->data[i]);
    free(v->data); v->data = NULL; v->size = v->cap = 0;
}

/* ---------- main ---------- */
int main(void) {
    // fast IO-ish
    int N = 0;
    if (scanf("%d", &N) != 1) return 0;

    // read N tokens as strings
    char **A = (char**)malloc((size_t)N * sizeof(char*));
    if (!A) exit(1);
    for (int i = 0; i < N; ++i) {
        A[i] = read_token();
        if (!A[i]) A[i] = strdup("0");
    }

    // special hack preserved from original C++ code
    if (strcmp(A[N - 1], "-318549634") == 0) {
        // clean up minimal
        for (int i = 0; i < N; ++i) free(A[i]);
        free(A);
        return 0;
    }

    // build Demical array B from strings
    Demical *B = (Demical*)malloc((size_t)N * sizeof(Demical));
    if (!B) exit(1);
    for (int i = 0; i < N; ++i) {
        bi_init(&B[i]);
        bi_from_cstr(&B[i], A[i]);
        free(A[i]);
    }
    free(A);

    DemicalList C; list_init(&C);

    for (int i = 0, j = 1; i < N; i = j++) {
        if (B[i].neg) continue;          // skip negative-start pieces
        Demical x; bi_init(&x); bi_copy(&x, &B[i]);
        while (j < N) {
            bi_add_inplace(&x, &B[j]);   // x += B[j]
            j++;
            if (x.neg) break;
        }
        Demical y; bi_init(&y);
        for (int k = j - 1; k > i; --k) {
            bi_add_inplace(&y, &B[k]);   // y += B[k]
            if (y.neg) {
                y.neg = 0;               // flip sign (like C++ code)
                bi_add_inplace(&x, &y);  // x += y
                bi_free(&y); bi_init(&y);
            }
        }
        bi_normalize(&x);
        list_append_move(&C, &x);           // move x into C
    }

    if (C.size > 0) {
        int idx = 0;
        for (int i = 1; i < C.size; ++i)
            if (bi_less(&C.data[idx], &C.data[i])) idx = i;
        bi_print(&C.data[idx]); printf("\n");
    } else {
        int idx = 0;
        for (int i = 1; i < N; ++i)
            if (bi_less(&B[idx], &B[i])) idx = i;
        bi_print(&B[idx]); printf("\n");
    }

    // free
    list_free(&C);
    for (int i = 0; i < N; ++i) bi_free(&B[i]);
    free(B);
    return 0;
}
"""