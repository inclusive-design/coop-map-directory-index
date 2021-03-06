from django.contrib.gis.db import models


class Ecosystem2020Questions(models.Model):
    column_name = models.CharField(max_length=2)
    question = models.CharField(max_length=254, blank=True,)

    class Meta:
        managed = False
        db_table = 'surveys_ecosystem2020_questions'


class Ecosystem2020(models.Model):
    a = models.DateTimeField(auto_now=True)
    b = models.CharField(max_length=254, blank=True,)
    c = models.CharField(max_length=254, blank=True,)
    d = models.CharField(max_length=254, blank=True,)
    e = models.CharField(max_length=254, blank=True,)
    f = models.CharField(max_length=254, blank=True,)
    g = models.CharField(max_length=254, blank=True,)
    h = models.CharField(max_length=254, blank=True,)
    i = models.CharField(max_length=254, blank=True,)
    j = models.CharField(max_length=254, blank=True,)
    k = models.CharField(max_length=254, blank=True,)
    l = models.CharField(max_length=254, blank=True,)
    m = models.CharField(max_length=254, blank=True,)
    n = models.CharField(max_length=254, blank=True,)
    o = models.CharField(max_length=254, blank=True,)
    p = models.CharField(max_length=254, blank=True,)
    q = models.CharField(max_length=254, blank=True,)
    r = models.CharField(max_length=254, blank=True,)
    s = models.CharField(max_length=254, blank=True,)
    t = models.CharField(max_length=254, blank=True,)
    u = models.CharField(max_length=254, blank=True,)
    v = models.CharField(max_length=254, blank=True,)
    w = models.CharField(max_length=254, blank=True,)
    x = models.CharField(max_length=254, blank=True,)
    y = models.CharField(max_length=254, blank=True,)
    z = models.CharField(max_length=254, blank=True,)
    aa = models.CharField(max_length=254, blank=True,)
    ab = models.CharField(max_length=254, blank=True,)
    ac = models.CharField(max_length=254, blank=True,)
    ad = models.CharField(max_length=254, blank=True,)
    ae = models.CharField(max_length=254, blank=True,)
    af = models.CharField(max_length=254, blank=True,)
    ag = models.CharField(max_length=254, blank=True,)
    ah = models.CharField(max_length=254, blank=True,)
    ai = models.CharField(max_length=254, blank=True,)
    aj = models.CharField(max_length=254, blank=True,)
    ak = models.CharField(max_length=254, blank=True,)
    al = models.CharField(max_length=254, blank=True,)
    am = models.CharField(max_length=254, blank=True,)
    an = models.CharField(max_length=254, blank=True,)
    ao = models.CharField(max_length=254, blank=True,)
    ap = models.CharField(max_length=254, blank=True,)
    aq = models.CharField(max_length=254, blank=True,)
    ar = models.CharField(max_length=254, blank=True,)
    as_field = models.CharField(max_length=254, blank=True,)  # Field renamed because it was a Python reserved word.
    at = models.CharField(max_length=254, blank=True,)
    au = models.CharField(max_length=254, blank=True,)
    av = models.CharField(max_length=254, blank=True,)
    aw = models.CharField(max_length=254, blank=True,)
    ax = models.CharField(max_length=254, blank=True,)
    ay = models.CharField(max_length=254, blank=True,)
    az = models.CharField(max_length=254, blank=True,)
    ba = models.CharField(max_length=254, blank=True,)
    bb = models.CharField(max_length=254, blank=True,)
    bc = models.CharField(max_length=254, blank=True,)
    bd = models.CharField(max_length=254, blank=True,)
    be = models.CharField(max_length=254, blank=True,)
    bf = models.CharField(max_length=254, blank=True,)
    bg = models.TextField(blank=True,)
    bh = models.CharField(max_length=254, blank=True,)
    bi = models.CharField(max_length=254, blank=True,)
    bj = models.CharField(max_length=254, blank=True,)
    bk = models.CharField(max_length=254, blank=True,)
    bl = models.CharField(max_length=254, blank=True,)
    bm = models.CharField(max_length=254, blank=True,)
    bn = models.CharField(max_length=254, blank=True,)
    bo = models.CharField(max_length=254, blank=True,)
    bp = models.CharField(max_length=254, blank=True,)
    bq = models.CharField(max_length=254, blank=True,)
    br = models.CharField(max_length=254, blank=True,)
    bs = models.CharField(max_length=254, blank=True,)
    bt = models.CharField(max_length=254, blank=True,)
    bu = models.CharField(max_length=254, blank=True,)
    bv = models.CharField(max_length=254, blank=True,)
    bw = models.CharField(max_length=254, blank=True,)
    bx = models.CharField(max_length=254, blank=True,)
    by = models.CharField(max_length=254, blank=True,)
    bz = models.CharField(max_length=254, blank=True,)
    ca = models.CharField(max_length=254, blank=True,)
    cb = models.CharField(max_length=254, blank=True,)
    cc = models.CharField(max_length=254, blank=True,)
    cd = models.CharField(max_length=254, blank=True,)
    ce = models.CharField(max_length=254, blank=True,)

    class Meta:
        managed = True
        db_table = 'surveys_ecosystem2020'
