# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class KioskoSaleorder(models.Model):
    create_date = models.DateTimeField()
    write_uid = models.IntegerField()
    client_order_ref = models.CharField(max_length=200)
    date_order = models.DateTimeField()
    partner_id = models.IntegerField()
    amount_tax = models.FloatField()
    procurement_group_id = models.IntegerField()
    amount_untaxed = models.FloatField()
    message_last_post = models.DateTimeField()
    company_id = models.IntegerField()
    state = models.CharField(max_length=200)
    pricelist_id = models.IntegerField()
    create_uid = models.IntegerField()
    write_date = models.DateTimeField()
    partner_invoice_id = models.IntegerField()
    user_id = models.IntegerField()
    date_confirm = models.DateField()
    amount_total = models.FloatField()
    name = models.CharField(max_length=200)
    partner_shipping_id = models.IntegerField()
    order_policy = models.CharField(max_length=200)
    picking_policy = models.CharField(max_length=200)
    warehouse_id = models.IntegerField()
    shipped = models.BooleanField()
    commitment_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Kiosko_saleorder'


class AccountAccount(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=64)
    create_date = models.DateTimeField(blank=True, null=True)
    reconcile = models.NullBooleanField()
    user_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING, db_column='user_type')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    shortcut = models.CharField(max_length=12, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    level = models.IntegerField(blank=True, null=True)
    currency_mode = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_account'
        unique_together = (('code', 'company'),)


class AccountAccountConsolRel(models.Model):
    child = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    parent = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_consol_rel'
        unique_together = (('child', 'parent'),)


class AccountAccountFinancialReport(models.Model):
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    report_line = models.ForeignKey('AccountFinancialReport', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_financial_report'
        unique_together = (('account', 'report_line'),)


class AccountAccountFinancialReportType(models.Model):
    report = models.ForeignKey('AccountFinancialReport', models.DO_NOTHING)
    account_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_financial_report_type'
        unique_together = (('report', 'account_type'),)


class AccountAccountTaxDefaultRel(models.Model):
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tax_default_rel'
        unique_together = (('account', 'tax'),)


class AccountAccountTemplate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=64)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    user_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING, db_column='user_type')
    chart_template = models.ForeignKey('AccountChartTemplate', models.DO_NOTHING, blank=True, null=True)
    shortcut = models.CharField(max_length=12, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    nocreate = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    reconcile = models.NullBooleanField()
    type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_account_template'


class AccountAccountTemplateTaxRel(models.Model):
    account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_template_tax_rel'
        unique_together = (('account', 'tax'),)


class AccountAccountType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=32)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    close_method = models.CharField(max_length=-1)
    report_type = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account_type'


class AccountAccountTypeRel(models.Model):
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_type_rel'
        unique_together = (('journal', 'account'),)


class AccountAddtmplWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    cparent = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_addtmpl_wizard'


class AccountAgedTrialBalance(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    period_length = models.IntegerField()
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    direction_selection = models.CharField(max_length=-1)
    result_selection = models.CharField(max_length=-1)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey('AccountFiscalyear', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_aged_trial_balance'


class AccountAgedTrialBalanceJournalRel(models.Model):
    account = models.ForeignKey(AccountAgedTrialBalance, models.DO_NOTHING)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_aged_trial_balance_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountAnalyticAccount(models.Model):
    code = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    quantity_max = models.FloatField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1)
    manager = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=-1)
    description = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    template = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_account'


class AccountAnalyticBalance(models.Model):
    date1 = models.DateField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    date2 = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    empty_acc = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_balance'


class AccountAnalyticChart(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_chart'


class AccountAnalyticCostLedger(models.Model):
    date1 = models.DateField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    date2 = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_cost_ledger'


class AccountAnalyticCostLedgerJournalReport(models.Model):
    date1 = models.DateField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    date2 = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_cost_ledger_journal_report'


class AccountAnalyticInvertedBalance(models.Model):
    date1 = models.DateField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    date2 = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_inverted_balance'


class AccountAnalyticJournal(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_analytic_journal'


class AccountAnalyticJournalName(models.Model):
    journal_line = models.ForeignKey('AccountAnalyticJournalReport', models.DO_NOTHING)
    journal_print = models.ForeignKey(AccountAnalyticJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_journal_name'
        unique_together = (('journal_line', 'journal_print'),)


class AccountAnalyticJournalReport(models.Model):
    date1 = models.DateField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    date2 = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_journal_report'


class AccountAnalyticLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    unit_amount = models.FloatField(blank=True, null=True)
    date = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=8, blank=True, null=True)
    general_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey(AccountAnalyticJournal, models.DO_NOTHING)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    move = models.ForeignKey('AccountMoveLine', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_line'


class AccountAutomaticReconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    power = models.IntegerField()
    max_amount = models.FloatField(blank=True, null=True)
    unreconciled = models.IntegerField(blank=True, null=True)
    reconciled = models.IntegerField(blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    allow_write_off = models.NullBooleanField()
    writeoff_acc = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    period = models.ForeignKey('AccountPeriod', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_automatic_reconcile'


class AccountBalanceReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    display_account = models.CharField(max_length=-1)
    date_from = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey('AccountFiscalyear', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_balance_report'


class AccountBalanceReportJournalRel(models.Model):
    account = models.ForeignKey(AccountBalanceReport, models.DO_NOTHING)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_balance_report_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountBankAccountsWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    bank_account = models.ForeignKey('WizardMultiChartsAccounts', models.DO_NOTHING)
    acc_name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    account_type = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_accounts_wizard'


class AccountBankStatement(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    balance_start = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    state = models.CharField(max_length=-1)
    period = models.ForeignKey('AccountPeriod', models.DO_NOTHING)
    total_entry_encoding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField()
    name = models.CharField(max_length=-1, blank=True, null=True)
    closing_date = models.DateTimeField(blank=True, null=True)
    balance_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance_end_real = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pos_session = models.ForeignKey('PosSession', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement'


class AccountBankStatementLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    statement = models.ForeignKey(AccountBankStatement, models.DO_NOTHING)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    partner_name = models.CharField(max_length=-1, blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    journal_entry = models.ForeignKey('AccountMove', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    pos_statement = models.ForeignKey('PosOrder', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_line'


class AccountCashboxLine(models.Model):
    bank_statement = models.ForeignKey(AccountBankStatement, models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    pieces = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    number_closing = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    number_opening = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_cashbox_line'


class AccountCentralJournal(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    date_from = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey('AccountFiscalyear', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    amount_currency = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_central_journal'


class AccountCentralJournalJournalRel(models.Model):
    account = models.ForeignKey(AccountCentralJournal, models.DO_NOTHING)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_central_journal_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountChangeCurrency(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_change_currency'


class AccountChart(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    target_move = models.CharField(max_length=-1)
    fiscalyear = models.ForeignKey('AccountFiscalyear', models.DO_NOTHING, db_column='fiscalyear', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_chart'


class AccountChartTemplate(models.Model):
    property_account_income_opening = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, db_column='property_account_income_opening', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    visible = models.NullBooleanField()
    tax_code_root = models.ForeignKey('AccountTaxCodeTemplate', models.DO_NOTHING, blank=True, null=True)
    property_account_income = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, db_column='property_account_income', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    complete_tax_set = models.NullBooleanField()
    property_account_payable = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, db_column='property_account_payable', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    bank_account_view = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_expense_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, db_column='property_account_expense_categ', blank=True, null=True)
    property_account_expense_opening = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, db_column='property_account_expense_opening', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    property_account_income_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, db_column='property_account_income_categ', blank=True, null=True)
    code_digits = models.IntegerField()
    name = models.CharField(max_length=-1)
    property_account_expense = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, db_column='property_account_expense', blank=True, null=True)
    property_account_receivable = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, db_column='property_account_receivable', blank=True, null=True)
    account_root = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_chart_template'


class AccountCommonAccountReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    display_account = models.CharField(max_length=-1)
    date_from = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey('AccountFiscalyear', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_common_account_report'


class AccountCommonAccountReportAccountJournalRel(models.Model):
    account_common_account_report = models.ForeignKey(AccountCommonAccountReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_account_report_account_journal_rel'
        unique_together = (('account_common_account_report', 'account_journal'),)


class AccountCommonJournalReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    date_from = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey('AccountFiscalyear', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    amount_currency = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_common_journal_report'


class AccountCommonJournalReportAccountJournalRel(models.Model):
    account_common_journal_report = models.ForeignKey(AccountCommonJournalReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_journal_report_account_journal_rel'
        unique_together = (('account_common_journal_report', 'account_journal'),)


class AccountCommonPartnerReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    result_selection = models.CharField(max_length=-1)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey('AccountFiscalyear', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_common_partner_report'


class AccountCommonPartnerReportAccountJournalRel(models.Model):
    account_common_partner_report = models.ForeignKey(AccountCommonPartnerReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_partner_report_account_journal_rel'
        unique_together = (('account_common_partner_report', 'account_journal'),)


class AccountCommonReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    date_from = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey('AccountFiscalyear', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_common_report'


class AccountCommonReportAccountJournalRel(models.Model):
    account_common_report = models.ForeignKey(AccountCommonReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_report_account_journal_rel'
        unique_together = (('account_common_report', 'account_journal'),)


class AccountConfigSettings(models.Model):
    date_stop = models.DateField()
    sale_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    module_account_voucher = models.NullBooleanField()
    module_account_asset = models.NullBooleanField()
    period = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    module_account_accountant = models.NullBooleanField()
    module_account_followup = models.NullBooleanField()
    purchase_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    has_chart_of_accounts = models.NullBooleanField()
    sale_refund_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    complete_tax_set = models.NullBooleanField()
    module_account_budget = models.NullBooleanField()
    date_start = models.DateField()
    purchase_refund_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    group_check_supplier_invoice_total = models.NullBooleanField()
    group_multi_currency = models.NullBooleanField()
    group_proforma_invoices = models.NullBooleanField()
    default_purchase_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, db_column='default_purchase_tax', blank=True, null=True)
    module_product_email_template = models.NullBooleanField()
    has_default_company = models.NullBooleanField()
    purchase_tax_rate = models.FloatField(blank=True, null=True)
    decimal_precision = models.IntegerField(blank=True, null=True)
    default_sale_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, db_column='default_sale_tax', blank=True, null=True)
    has_fiscal_year = models.NullBooleanField()
    module_account_payment = models.NullBooleanField()
    sale_tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, db_column='sale_tax', blank=True, null=True)
    purchase_tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, db_column='purchase_tax', blank=True, null=True)
    module_account_check_writing = models.NullBooleanField()
    code_digits = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_tax_rate = models.FloatField(blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING, blank=True, null=True)
    group_analytic_accounting = models.NullBooleanField()
    module_payment_paypal = models.NullBooleanField()
    module_payment_buckaroo = models.NullBooleanField()
    module_payment_adyen = models.NullBooleanField()
    module_payment_ogone = models.NullBooleanField()
    group_analytic_account_for_sales = models.NullBooleanField()
    module_sale_analytic_plans = models.NullBooleanField()
    group_payment_options = models.NullBooleanField()
    module_purchase_analytic_plans = models.NullBooleanField()
    group_analytic_account_for_purchases = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_config_settings'


class AccountFinancialReport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    account_report = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    style_overwrite = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    display_detail = models.CharField(max_length=-1, blank=True, null=True)
    sign = models.IntegerField()
    type = models.CharField(max_length=-1, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_financial_report'


class AccountFiscalPosition(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    country_group = models.ForeignKey('ResCountryGroup', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    auto_apply = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    vat_required = models.NullBooleanField()
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_fiscal_position'


class AccountFiscalPositionAccount(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    account_dest = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    account_src = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_account'
        unique_together = (('position', 'account_src', 'account_dest'),)


class AccountFiscalPositionAccountTemplate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    position = models.ForeignKey('AccountFiscalPositionTemplate', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    account_dest = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    account_src = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_account_template'


class AccountFiscalPositionTax(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING)
    tax_src = models.ForeignKey('AccountTax', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    tax_dest = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_tax'
        unique_together = (('position', 'tax_src', 'tax_dest'),)


class AccountFiscalPositionTaxTemplate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    position = models.ForeignKey('AccountFiscalPositionTemplate', models.DO_NOTHING)
    tax_src = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    tax_dest = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_tax_template'


class AccountFiscalPositionTemplate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_template'


class AccountFiscalyear(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    date_stop = models.DateField()
    code = models.CharField(max_length=6)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    end_journal_period = models.ForeignKey('AccountJournalPeriod', models.DO_NOTHING, blank=True, null=True)
    date_start = models.DateField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscalyear'


class AccountFiscalyearClose(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    report_name = models.CharField(max_length=-1)
    fy2 = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING)
    period = models.ForeignKey('AccountPeriod', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    fy = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscalyear_close'


class AccountFiscalyearCloseState(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    fy = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscalyear_close_state'


class AccountGeneralJournal(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    date_from = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    amount_currency = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_general_journal'


class AccountGeneralJournalJournalRel(models.Model):
    account = models.ForeignKey(AccountGeneralJournal, models.DO_NOTHING)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_general_journal_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountInstaller(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    date_stop = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    date_start = models.DateField()
    charts = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    period = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    has_default_company = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_installer'


class AccountInvoice(models.Model):
    comment = models.TextField(blank=True, null=True)
    date_due = models.DateField(blank=True, null=True)
    check_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    reference = models.CharField(max_length=-1, blank=True, null=True)
    payment_term = models.ForeignKey('AccountPaymentTerm', models.DO_NOTHING, db_column='payment_term', blank=True, null=True)
    number = models.CharField(max_length=-1, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, db_column='fiscal_position', blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    partner_bank = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    supplier_invoice_number = models.CharField(max_length=-1, blank=True, null=True)
    reference_type = models.CharField(max_length=-1)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    move = models.ForeignKey('AccountMove', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    internal_number = models.CharField(max_length=-1, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    reconciled = models.NullBooleanField()
    residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    move_name = models.CharField(max_length=-1, blank=True, null=True)
    date_invoice = models.DateField(blank=True, null=True)
    period = models.ForeignKey('AccountPeriod', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    origin = models.CharField(max_length=-1, blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    sent = models.NullBooleanField()
    commercial_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    section = models.ForeignKey('CrmCaseSection', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice'
        unique_together = (('number', 'company', 'journal', 'type'),)


class AccountInvoiceCancel(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_cancel'


class AccountInvoiceConfirm(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_confirm'


class AccountInvoiceLine(models.Model):
    origin = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    uos = models.ForeignKey('ProductUom', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING, blank=True, null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    account_analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    name = models.TextField()
    purchase_line = models.ForeignKey('PurchaseOrderLine', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_line'


class AccountInvoiceLineTax(models.Model):
    invoice_line = models.ForeignKey(AccountInvoiceLine, models.DO_NOTHING)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_invoice_line_tax'
        unique_together = (('invoice_line', 'tax'),)


class AccountInvoiceRefund(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    filter_refund = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=-1)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    period = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_refund'


class AccountInvoiceTax(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING, blank=True, null=True)
    manual = models.NullBooleanField()
    base_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    tax_code = models.ForeignKey('AccountTaxCode', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    base = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    account_analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    base_code = models.ForeignKey('AccountTaxCode', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_invoice_tax'


class AccountJournal(models.Model):
    code = models.CharField(max_length=5)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    loss_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, db_column='currency', blank=True, null=True)
    internal_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    cash_control = models.NullBooleanField()
    centralisation = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    profit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=32)
    default_debit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    default_credit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    sequence = models.ForeignKey('IrSequence', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    allow_date = models.NullBooleanField()
    update_posted = models.NullBooleanField()
    name = models.CharField(max_length=-1)
    analytic_journal = models.ForeignKey(AccountAnalyticJournal, models.DO_NOTHING, blank=True, null=True)
    with_last_closing_balance = models.NullBooleanField()
    entry_posted = models.NullBooleanField()
    group_invoice_lines = models.NullBooleanField()
    self_checkout_payment_method = models.NullBooleanField()
    journal_user = models.NullBooleanField()
    amount_authorized_diff = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal'
        unique_together = (('name', 'company'), ('code', 'company'),)


class AccountJournalAccountVatDeclarationRel(models.Model):
    account_vat_declaration = models.ForeignKey('AccountVatDeclaration', models.DO_NOTHING)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_vat_declaration_rel'
        unique_together = (('account_vat_declaration', 'account_journal'),)


class AccountJournalAccountingReportRel(models.Model):
    accounting_report = models.ForeignKey('AccountingReport', models.DO_NOTHING)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_accounting_report_rel'
        unique_together = (('accounting_report', 'account_journal'),)


class AccountJournalCashboxLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    pieces = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal_cashbox_line'


class AccountJournalGroupRel(models.Model):
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_group_rel'
        unique_together = (('journal', 'group'),)


class AccountJournalPeriod(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    state = models.CharField(max_length=-1)
    period = models.ForeignKey('AccountPeriod', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal_period'


class AccountJournalSelect(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal_select'


class AccountJournalTypeRel(models.Model):
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    type = models.ForeignKey(AccountAccountType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_type_rel'
        unique_together = (('journal', 'type'),)


class AccountModel(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    legend = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_model'


class AccountModelLine(models.Model):
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    model = models.ForeignKey(AccountModel, models.DO_NOTHING)
    create_date = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_maturity = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_currency = models.FloatField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_model_line'


class AccountMove(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    state = models.CharField(max_length=-1)
    period = models.ForeignKey('AccountPeriod', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    narration = models.TextField(blank=True, null=True)
    date = models.DateField()
    balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    to_check = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_move'


class AccountMoveBankReconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_bank_reconcile'


class AccountMoveLine(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    statement = models.ForeignKey(AccountBankStatement, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    date_maturity = models.DateField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    reconcile_partial = models.ForeignKey('AccountMoveReconcile', models.DO_NOTHING, blank=True, null=True)
    blocked = models.NullBooleanField()
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    centralisation = models.CharField(max_length=8, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    reconcile_ref = models.CharField(max_length=-1, blank=True, null=True)
    tax_code = models.ForeignKey('AccountTaxCode', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    period = models.ForeignKey('AccountPeriod', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    date = models.DateField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    move = models.ForeignKey(AccountMove, models.DO_NOTHING)
    name = models.CharField(max_length=-1)
    reconcile = models.ForeignKey('AccountMoveReconcile', models.DO_NOTHING, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    account_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line'


class AccountMoveLineReconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    writeoff = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    trans_nbr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line_reconcile'


class AccountMoveLineReconcileSelect(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line_reconcile_select'


class AccountMoveLineReconcileWriteoff(models.Model):
    comment = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    writeoff_acc = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_p = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line_reconcile_writeoff'


class AccountMoveLineRelation(models.Model):
    move = models.ForeignKey('AccountStatementFromInvoiceLines', models.DO_NOTHING)
    line = models.ForeignKey(AccountMoveLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_line_relation'
        unique_together = (('move', 'line'),)


class AccountMoveLineUnreconcileSelect(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line_unreconcile_select'


class AccountMoveReconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    opening_reconciliation = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_move_reconcile'


class AccountOpenClosedFiscalyear(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    fyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_open_closed_fiscalyear'


class AccountPartnerBalance(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    display_partner = models.CharField(max_length=-1, blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    result_selection = models.CharField(max_length=-1)
    date_from = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_partner_balance'


class AccountPartnerBalanceJournalRel(models.Model):
    account = models.ForeignKey(AccountPartnerBalance, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_partner_balance_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountPartnerLedger(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    initial_balance = models.NullBooleanField()
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    page_split = models.NullBooleanField()
    period_to = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    result_selection = models.CharField(max_length=-1)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey('AccountPeriod', models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    amount_currency = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_partner_ledger'


class AccountPartnerLedgerJournalRel(models.Model):
    account = models.ForeignKey(AccountPartnerLedger, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_partner_ledger_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountPartnerReconcileProcess(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    next_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    to_reconcile = models.FloatField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    today_reconciled = models.FloatField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    progress = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_partner_reconcile_process'


class AccountPaymentTerm(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_payment_term'


class AccountPaymentTermLine(models.Model):
    payment = models.ForeignKey(AccountPaymentTerm, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    days2 = models.IntegerField()
    days = models.IntegerField()
    value = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    value_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_term_line'


class AccountPeriod(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    date_stop = models.DateField()
    code = models.CharField(max_length=12, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    date_start = models.DateField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    fiscalyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING)
    state = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    special = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_period'
        unique_together = (('name', 'company'),)


class AccountPeriodClose(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    sure = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_period_close'


class AccountPrintJournal(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    sort_selection = models.CharField(max_length=-1)
    date_from = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    amount_currency = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_print_journal'


class AccountPrintJournalJournalRel(models.Model):
    account = models.ForeignKey(AccountPrintJournal, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_print_journal_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountReportGeneralLedger(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    initial_balance = models.NullBooleanField()
    target_move = models.CharField(max_length=-1)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    display_account = models.CharField(max_length=-1)
    date_from = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING, blank=True, null=True)
    sortby = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    amount_currency = models.NullBooleanField()
    landscape = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_report_general_ledger'


class AccountReportGeneralLedgerJournalRel(models.Model):
    account = models.ForeignKey(AccountReportGeneralLedger, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_report_general_ledger_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountSequenceFiscalyear(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    fiscalyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    sequence = models.ForeignKey('IrSequence', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    sequence_main = models.ForeignKey('IrSequence', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_sequence_fiscalyear'


class AccountStateOpen(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_state_open'


class AccountStatementFromInvoiceLines(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_statement_from_invoice_lines'


class AccountStatementOperationTemplate(models.Model):
    amount_type = models.CharField(max_length=-1)
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    label = models.CharField(max_length=-1, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_statement_operation_template'


class AccountSubscription(models.Model):
    model = models.ForeignKey(AccountModel, models.DO_NOTHING)
    period_nbr = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    date_start = models.DateField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    period_total = models.IntegerField()
    state = models.CharField(max_length=-1)
    period_type = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_subscription'


class AccountSubscriptionGenerate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'account_subscription_generate'


class AccountSubscriptionLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField()
    subscription = models.ForeignKey(AccountSubscription, models.DO_NOTHING)
    move = models.ForeignKey(AccountMove, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_subscription_line'


class AccountTax(models.Model):
    domain = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    account_analytic_paid = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    ref_tax_code = models.ForeignKey('AccountTaxCode', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    account_paid = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    base_sign = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    child_depend = models.NullBooleanField()
    include_base_amount = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    ref_tax_sign = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    applicable_type = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    tax_code = models.ForeignKey('AccountTaxCode', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    python_compute_inv = models.TextField(blank=True, null=True)
    python_applicable = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=-1)
    ref_base_sign = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    type_tax_use = models.CharField(max_length=-1)
    base_code = models.ForeignKey('AccountTaxCode', models.DO_NOTHING, blank=True, null=True)
    account_analytic_collected = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    ref_base_code = models.ForeignKey('AccountTaxCode', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    account_collected = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    python_compute = models.TextField(blank=True, null=True)
    tax_sign = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_include = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_tax'
        unique_together = (('name', 'company'),)


class AccountTaxChart(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    period = models.ForeignKey(AccountPeriod, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_tax_chart'


class AccountTaxCode(models.Model):
    info = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=64, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    sign = models.FloatField()
    notprintable = models.NullBooleanField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_code'


class AccountTaxCodeTemplate(models.Model):
    info = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=64, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    sign = models.FloatField()
    notprintable = models.NullBooleanField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_code_template'


class AccountTaxTemplate(models.Model):
    domain = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    ref_tax_code = models.ForeignKey(AccountTaxCodeTemplate, models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    base_sign = models.FloatField(blank=True, null=True)
    child_depend = models.NullBooleanField()
    include_base_amount = models.NullBooleanField()
    applicable_type = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    ref_base_code = models.ForeignKey(AccountTaxCodeTemplate, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    tax_code = models.ForeignKey(AccountTaxCodeTemplate, models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    python_compute_inv = models.TextField(blank=True, null=True)
    ref_tax_sign = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=-1)
    ref_base_sign = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    type_tax_use = models.CharField(max_length=-1)
    base_code = models.ForeignKey(AccountTaxCodeTemplate, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    python_applicable = models.TextField(blank=True, null=True)
    account_paid = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    account_collected = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    python_compute = models.TextField(blank=True, null=True)
    tax_sign = models.FloatField(blank=True, null=True)
    price_include = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account_tax_template'


class AccountTemplateFinancialReport(models.Model):
    account_template = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    report_line = models.ForeignKey(AccountFinancialReport, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_template_financial_report'
        unique_together = (('account_template', 'report_line'),)


class AccountUnreconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_unreconcile'


class AccountUnreconcileReconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_unreconcile_reconcile'


class AccountUseModel(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_use_model'


class AccountUseModelRelation(models.Model):
    account = models.ForeignKey(AccountUseModel, models.DO_NOTHING)
    model = models.ForeignKey(AccountModel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_use_model_relation'
        unique_together = (('account', 'model'),)


class AccountVatDeclaration(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    period_to = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    filter = models.CharField(max_length=-1)
    period_from = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    fiscalyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    based_on = models.CharField(max_length=-1)
    display_detail = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    chart_tax = models.ForeignKey(AccountTaxCode, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'account_vat_declaration'


class AccountVoucher(models.Model):
    comment = models.CharField(max_length=-1)
    date_due = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    is_multi_currency = models.NullBooleanField()
    number = models.CharField(max_length=-1, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    narration = models.TextField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    payment_rate_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    reference = models.CharField(max_length=-1, blank=True, null=True)
    pay_now = models.CharField(max_length=-1, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    writeoff_acc = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    pre_line = models.NullBooleanField()
    type = models.CharField(max_length=-1, blank=True, null=True)
    payment_option = models.CharField(max_length=-1)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    period = models.ForeignKey(AccountPeriod, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    move = models.ForeignKey(AccountMove, models.DO_NOTHING, blank=True, null=True)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING, blank=True, null=True)
    payment_rate = models.DecimalField(max_digits=65535, decimal_places=65535)
    name = models.CharField(max_length=-1, blank=True, null=True)
    analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'account_voucher'


class AccountVoucherLine(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    reconcile = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    amount_unreconciled = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    untax_amount = models.FloatField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    account_analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    voucher = models.ForeignKey(AccountVoucher, models.DO_NOTHING)
    amount_original = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    move_line = models.ForeignKey(AccountMoveLine, models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_voucher_line'


class AccountingReport(models.Model):
    period_to_cmp = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_to_cmp', blank=True, null=True)
    chart_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    period_from_cmp = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_from_cmp', blank=True, null=True)
    account_report = models.ForeignKey(AccountFinancialReport, models.DO_NOTHING)
    period_to = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_to', blank=True, null=True)
    date_to_cmp = models.DateField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    fiscalyear = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    fiscalyear_id_cmp = models.ForeignKey(AccountFiscalyear, models.DO_NOTHING, db_column='fiscalyear_id_cmp', blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    period_from = models.ForeignKey(AccountPeriod, models.DO_NOTHING, db_column='period_from', blank=True, null=True)
    label_filter = models.CharField(max_length=-1, blank=True, null=True)
    filter_cmp = models.CharField(max_length=-1)
    enable_filter = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    filter = models.CharField(max_length=-1)
    date_from_cmp = models.DateField(blank=True, null=True)
    debit_credit = models.NullBooleanField()
    target_move = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'accounting_report'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BaseConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    module_google_drive = models.NullBooleanField()
    module_base_import = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    module_portal = models.NullBooleanField()
    module_google_calendar = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    module_share = models.NullBooleanField()
    font = models.ForeignKey('ResFont', models.DO_NOTHING, db_column='font', blank=True, null=True)
    module_auth_oauth = models.NullBooleanField()
    module_multi_company = models.NullBooleanField()
    alias_domain = models.CharField(max_length=-1, blank=True, null=True)
    auth_signup_reset_password = models.NullBooleanField()
    auth_signup_uninvited = models.NullBooleanField()
    auth_signup_template_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    group_note_fancy = models.NullBooleanField()
    module_note_pad = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'base_config_settings'


class BaseExternalMapping(models.Model):
    model = models.ForeignKey('IrModel', models.DO_NOTHING)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=64)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_external_mapping'


class BaseExternalMappingLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    external_field = models.CharField(max_length=32)
    in_function = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    external_type = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    out_function = models.TextField(blank=True, null=True)
    field = models.ForeignKey('IrModelFields', models.DO_NOTHING)
    update = models.NullBooleanField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    mapping = models.ForeignKey(BaseExternalMapping, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    translate = models.NullBooleanField()
    type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'base_external_mapping_line'


class BaseImportImport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    file_type = models.CharField(max_length=-1, blank=True, null=True)
    file_name = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    file = models.BinaryField(blank=True, null=True)
    res_model = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_import'


class BaseImportTestsModelsChar(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char'


class BaseImportTestsModelsCharNoreadonly(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_noreadonly'


class BaseImportTestsModelsCharReadonly(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_readonly'


class BaseImportTestsModelsCharRequired(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_required'


class BaseImportTestsModelsCharStates(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_states'


class BaseImportTestsModelsCharStillreadonly(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_stillreadonly'


class BaseImportTestsModelsM2O(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.ForeignKey('BaseImportTestsModelsM2ORelated', models.DO_NOTHING, db_column='value', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o'


class BaseImportTestsModelsM2ORelated(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_related'


class BaseImportTestsModelsM2ORequired(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.ForeignKey('BaseImportTestsModelsM2ORequiredRelated', models.DO_NOTHING, db_column='value')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_required'


class BaseImportTestsModelsM2ORequiredRelated(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_required_related'


class BaseImportTestsModelsO2M(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_o2m'


class BaseImportTestsModelsO2MChild(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey(BaseImportTestsModelsO2M, models.DO_NOTHING, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_o2m_child'


class BaseImportTestsModelsPreview(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    othervalue = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    somevalue = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_preview'


class BaseLanguageExport(models.Model):
    lang = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    format = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_export'


class BaseLanguageImport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    code = models.CharField(max_length=5)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    data = models.BinaryField()
    overwrite = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'base_language_import'


class BaseLanguageInstall(models.Model):
    lang = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    overwrite = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'base_language_install'


class BaseModuleConfiguration(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_configuration'


class BaseModuleUpdate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    updated = models.IntegerField(blank=True, null=True)
    added = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_update'


class BaseModuleUpgrade(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    module_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_upgrade'


class BaseReportDesignerInstaller(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    plugin_file = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_report_designer_installer'


class BaseReportFileSxw(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    report = models.ForeignKey('IrActReportXml', models.DO_NOTHING, blank=True, null=True)
    file_sxw_upload = models.BinaryField()
    file_sxw = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_report_file_sxw'


class BaseReportRmlSave(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    file_rml = models.BinaryField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_report_rml_save'


class BaseReportSxw(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    report = models.ForeignKey('IrActReportXml', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'base_report_sxw'


class BaseSetupTerminology(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    partner = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'base_setup_terminology'


class BaseUpdateTranslations(models.Model):
    lang = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_update_translations'


class BoardCreate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    menu_parent = models.ForeignKey('IrUiMenu', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'board_create'


class BusBus(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    message = models.CharField(max_length=-1, blank=True, null=True)
    channel = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_bus'


class CashBoxIn(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_date = models.DateTimeField(blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_box_in'


class CashBoxOut(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_box_out'


class ChangePasswordUser(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    user_login = models.CharField(max_length=-1, blank=True, null=True)
    new_passwd = models.CharField(max_length=-1, blank=True, null=True)
    wizard = models.ForeignKey('ChangePasswordWizard', models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'change_password_user'


class ChangePasswordWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_password_wizard'


class ChangeProductionQty(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'change_production_qty'


class CrmCaseSection(models.Model):
    code = models.CharField(unique=True, max_length=8, blank=True, null=True)
    working_hours = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    complete_name = models.CharField(max_length=256, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    change_responsible = models.NullBooleanField()
    name = models.CharField(max_length=64)
    reply_to = models.CharField(max_length=64, blank=True, null=True)
    use_quotations = models.NullBooleanField()
    invoiced_target = models.IntegerField(blank=True, null=True)
    invoiced_forecast = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_case_section'


class DecimalPrecision(models.Model):
    digits = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decimal_precision'


class DecimalPrecisionTest(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    float_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    float = models.FloatField(blank=True, null=True)
    float_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decimal_precision_test'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoConnect(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_connect'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoCreateModelWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    filename = models.CharField(max_length=32, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    file = models.BinaryField(blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING, db_column='model')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_create_model_wizard'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSqlUpdateWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    filename = models.CharField(max_length=32, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    file = models.BinaryField(blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING, db_column='model')
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_sql_update_wizard'


class EmailTemplate(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    auto_delete = models.NullBooleanField()
    mail_server = models.ForeignKey('IrMailServer', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    partner_to = models.CharField(max_length=-1, blank=True, null=True)
    ref_ir_act_window = models.ForeignKey('IrActWindow', models.DO_NOTHING, db_column='ref_ir_act_window', blank=True, null=True)
    subject = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    report_template = models.ForeignKey('IrActReportXml', models.DO_NOTHING, db_column='report_template', blank=True, null=True)
    ref_ir_value = models.ForeignKey('IrValues', models.DO_NOTHING, db_column='ref_ir_value', blank=True, null=True)
    user_signature = models.NullBooleanField()
    null_value = models.CharField(max_length=-1, blank=True, null=True)
    email_cc = models.CharField(max_length=-1, blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    sub_model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='sub_model_object_field', blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    email_to = models.CharField(max_length=-1, blank=True, null=True)
    sub_object = models.ForeignKey('IrModel', models.DO_NOTHING, db_column='sub_object', blank=True, null=True)
    copyvalue = models.CharField(max_length=-1, blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='model_object_field', blank=True, null=True)
    report_name = models.CharField(max_length=-1, blank=True, null=True)
    use_default_to = models.NullBooleanField()
    reply_to = models.CharField(max_length=-1, blank=True, null=True)
    model_0 = models.CharField(db_column='model', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    email_from = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_template'


class EmailTemplateAttachmentRel(models.Model):
    email_template = models.ForeignKey(EmailTemplate, models.DO_NOTHING)
    attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_template_attachment_rel'
        unique_together = (('email_template', 'attachment'),)


class EmailTemplatePreview(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    sub_object = models.ForeignKey('IrModel', models.DO_NOTHING, db_column='sub_object', blank=True, null=True)
    auto_delete = models.NullBooleanField()
    mail_server = models.ForeignKey('IrMailServer', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    partner_to = models.CharField(max_length=-1, blank=True, null=True)
    ref_ir_act_window = models.ForeignKey('IrActWindow', models.DO_NOTHING, db_column='ref_ir_act_window', blank=True, null=True)
    subject = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    report_template = models.ForeignKey('IrActReportXml', models.DO_NOTHING, db_column='report_template', blank=True, null=True)
    ref_ir_value = models.ForeignKey('IrValues', models.DO_NOTHING, db_column='ref_ir_value', blank=True, null=True)
    user_signature = models.NullBooleanField()
    null_value = models.CharField(max_length=-1, blank=True, null=True)
    email_cc = models.CharField(max_length=-1, blank=True, null=True)
    res_id = models.CharField(max_length=-1, blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    sub_model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='sub_model_object_field', blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    email_to = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    copyvalue = models.CharField(max_length=-1, blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='model_object_field', blank=True, null=True)
    report_name = models.CharField(max_length=-1, blank=True, null=True)
    use_default_to = models.NullBooleanField()
    reply_to = models.CharField(max_length=-1, blank=True, null=True)
    model_0 = models.CharField(db_column='model', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    email_from = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_template_preview'


class EmailTemplatePreviewResPartnerRel(models.Model):
    email_template_preview = models.ForeignKey(EmailTemplatePreview, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_template_preview_res_partner_rel'
        unique_together = (('email_template_preview', 'res_partner'),)


class FetchmailConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fetchmail_config_settings'


class FetchmailServer(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    active = models.NullBooleanField()
    port = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    configuration = models.TextField(blank=True, null=True)
    script = models.CharField(max_length=-1, blank=True, null=True)
    object = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    attach = models.NullBooleanField()
    state = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1)
    action = models.ForeignKey('IrActServer', models.DO_NOTHING, blank=True, null=True)
    user = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1)
    is_ssl = models.NullBooleanField()
    server = models.CharField(max_length=-1, blank=True, null=True)
    original = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'fetchmail_server'


class ImChatMessage(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    to = models.ForeignKey('ImChatSession', models.DO_NOTHING)
    write_date = models.DateTimeField(blank=True, null=True)
    message = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    from_field = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='from_id', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'im_chat_message'


class ImChatPresence(models.Model):
    status = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    last_presence = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    last_poll = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'im_chat_presence'


class ImChatSession(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(max_length=50, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'im_chat_session'


class ImChatSessionResUsersRel(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    session = models.ForeignKey(ImChatSession, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'im_chat_session_res_users_rel'


class IrActClient(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    params_store = models.BinaryField(blank=True, null=True)
    tag = models.CharField(max_length=-1)
    context = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ir_act_client'


class IrActReportXml(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    parser = models.CharField(max_length=-1, blank=True, null=True)
    header = models.NullBooleanField()
    report_type = models.CharField(max_length=-1)
    attachment = models.CharField(max_length=-1, blank=True, null=True)
    report_sxw_content_data = models.BinaryField(blank=True, null=True)
    report_xml = models.CharField(max_length=-1, blank=True, null=True)
    report_rml_content_data = models.BinaryField(blank=True, null=True)
    auto = models.NullBooleanField()
    report_file = models.CharField(max_length=-1, blank=True, null=True)
    multi = models.NullBooleanField()
    report_xsl = models.CharField(max_length=-1, blank=True, null=True)
    report_rml = models.CharField(max_length=-1, blank=True, null=True)
    report_name = models.CharField(max_length=-1)
    attachment_use = models.NullBooleanField()
    model = models.CharField(max_length=-1)
    paperformat = models.ForeignKey('ReportPaperformat', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_report_xml'


class IrActServer(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    code = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    crud_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    condition = models.CharField(max_length=-1, blank=True, null=True)
    ref_object = models.CharField(max_length=128, blank=True, null=True)
    id_object = models.CharField(max_length=128, blank=True, null=True)
    crud_model_name = models.CharField(max_length=-1, blank=True, null=True)
    use_relational_model = models.CharField(max_length=-1)
    use_create = models.CharField(max_length=-1)
    wkf_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, blank=True, null=True)
    wkf_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1)
    id_value = models.CharField(max_length=-1, blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING)
    sub_model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='sub_model_object_field', blank=True, null=True)
    link_new_record = models.NullBooleanField()
    wkf_transition = models.ForeignKey('WkfTransition', models.DO_NOTHING, blank=True, null=True)
    sub_object = models.ForeignKey('IrModel', models.DO_NOTHING, db_column='sub_object', blank=True, null=True)
    use_write = models.CharField(max_length=-1)
    wkf_model_name = models.CharField(max_length=-1, blank=True, null=True)
    copyvalue = models.CharField(max_length=-1, blank=True, null=True)
    write_expression = models.CharField(max_length=-1, blank=True, null=True)
    menu_ir_values = models.ForeignKey('IrValues', models.DO_NOTHING, blank=True, null=True)
    model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='model_object_field', blank=True, null=True)
    link_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, blank=True, null=True)
    template = models.ForeignKey(EmailTemplate, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_server'


class IrActUrl(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    target = models.CharField(max_length=-1)
    url = models.TextField()

    class Meta:
        managed = False
        db_table = 'ir_act_url'


class IrActWindow(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    domain = models.CharField(max_length=-1, blank=True, null=True)
    res_model = models.CharField(max_length=-1)
    search_view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    view_type = models.CharField(max_length=-1)
    src_model = models.CharField(max_length=-1, blank=True, null=True)
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    auto_refresh = models.IntegerField(blank=True, null=True)
    view_mode = models.CharField(max_length=-1)
    multi = models.NullBooleanField()
    target = models.CharField(max_length=-1, blank=True, null=True)
    auto_search = models.NullBooleanField()
    res_id = models.IntegerField(blank=True, null=True)
    filter = models.NullBooleanField()
    limit = models.IntegerField(blank=True, null=True)
    context = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ir_act_window'


class IrActWindowGroupRel(models.Model):
    act = models.ForeignKey(IrActWindow, models.DO_NOTHING)
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_act_window_group_rel'
        unique_together = (('act', 'gid'),)


class IrActWindowView(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    multi = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    view_mode = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    act_window = models.ForeignKey(IrActWindow, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_window_view'
        unique_together = (('act_window', 'view_mode'),)


class IrActions(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    help = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ir_actions'


class IrActionsTodo(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=-1)
    action_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ir_actions_todo'


class IrAttachment(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=1024, blank=True, null=True)
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    res_name = models.CharField(max_length=-1, blank=True, null=True)
    db_datas = models.BinaryField(blank=True, null=True)
    datas_fname = models.CharField(max_length=-1, blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=-1)
    res_id = models.IntegerField(blank=True, null=True)
    store_fname = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ir_attachment'


class IrConfigParameter(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    value = models.TextField()
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    key = models.CharField(unique=True, max_length=-1)

    class Meta:
        managed = False
        db_table = 'ir_config_parameter'


class IrConfigParameterGroupsRel(models.Model):
    icp = models.ForeignKey(IrConfigParameter, models.DO_NOTHING)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_config_parameter_groups_rel'
        unique_together = (('icp', 'group'),)


class IrCron(models.Model):
    function = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    args = models.TextField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    name = models.CharField(max_length=-1)
    interval_type = models.CharField(max_length=-1, blank=True, null=True)
    numbercall = models.IntegerField(blank=True, null=True)
    nextcall = models.DateTimeField()
    priority = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=-1, blank=True, null=True)
    doall = models.NullBooleanField()
    write_date = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    interval_number = models.IntegerField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_cron'


class IrDefault(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    ref_table = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    ref_id = models.IntegerField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    field_tbl = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    field_name = models.CharField(max_length=-1, blank=True, null=True)
    page = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_default'


class IrExports(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    resource = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_exports'


class IrExportsLine(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    export = models.ForeignKey(IrExports, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_exports_line'


class IrFieldsConverter(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_fields_converter'


class IrFilters(models.Model):
    model_id = models.CharField(max_length=-1)
    domain = models.TextField()
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    is_default = models.NullBooleanField()
    context = models.TextField()
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
