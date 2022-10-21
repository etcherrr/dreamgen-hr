from odoo import api, fields, models, exceptions, _

class applicantData(models.Model):
    _inherit = 'hr.applicant'

    def create_employee_data(self):
        """ Create an hr.employee from the hr.applicants """
        employee = False
        for applicant in self:
            contact_name = False
            if applicant.partner_id:
                address_id = applicant.partner_id.address_get(['contact'])['contact']
                contact_name = applicant.partner_id.display_name
            else:
                if not applicant.partner_name:
                    raise UserError(_('You must define a Contact Name for this applicant.'))
                new_partner_id = self.env['res.partner'].create({
                    'is_company': False,
                    'type': 'private',
                    'name': applicant.partner_name,
                    'email': applicant.email_from,
                    'phone': applicant.partner_phone,
                    'mobile': applicant.partner_mobile
                })
                applicant.partner_id = new_partner_id
                address_id = new_partner_id.address_get(['contact'])['contact']
            if applicant.partner_name or contact_name:
                employee_data = {
                    'default_name': applicant.partner_name or contact_name,
                    'default_job_id': applicant.job_id.id,
                    'default_job_title': applicant.job_id.name,
                    'default_address_home_id': address_id,
                    'default_place_of_birth': applicant.tempatlahir,
                    'default_birthday': applicant.tanggallahir,
                    'default_agama': applicant.agama,
                    'default_jenisklmn': applicant.gender,
                    'default_identification_id': applicant.nomorktp,
                    'default_alamatktp': applicant.alamatktp,
                    'default_alamatsaatini': applicant.alamatsaatini,
                    'default_emergency_contact': applicant.emergencycontact,
                    'default_emergency_phone': applicant.emergencyphone,
                    'default_image_1920' : applicant.pasfoto,
                    #INFORMASI KELUARGA
                    'default_namaayah': applicant.namaayah,
                    'default_tgllahirayah': applicant.tgllahirayah,
                    'default_pendidikanayah': applicant.pendidikanayah,
                    'default_pekerjaanayah': applicant.pekerjaanayah,
                    'default_namaibu': applicant.namaibu,
                    'default_tgllahiribu': applicant.tgllahiribu,
                    'default_pendidikanibu': applicant.pendidikanibu,
                    'default_pekerjaanibu': applicant.pekerjaanibu,
                    #INFORMASI PASANGAN#
                    'default_marital' : applicant.marital,
                    'default_namapasangan': applicant.namapasangan,
                    'default_tgllahirpasangan': applicant.tgllahirpasangan,
                    'default_pendpasangan': applicant.pendpasangan,
                    'default_pekpasangan': applicant.pekpasangan,
                    'default_jumlahanak': applicant.jumlahanak,
                    #Informasi Pendidikan 1#
                    'default_jenjang1' : applicant.jenjang1,
                    'default_namasekolah1': applicant.namasekolah1,
                    'default_jurusan': applicant.jurusan,
                    'default_kelulusan': applicant.kelulusan,
                    'default_tglmasukunv': applicant.tglmasukunv,
                    'default_tgllulus': applicant.tgllulus,
                    'default_ipk': applicant.ipk,
                    #Informasi Pendidikan 2#
                    'default_jenjang2' : applicant.jenjang2,
                    'default_namasekolah2': applicant.namasekolah2,
                    'default_jurusan2': applicant.jurusan2,
                    'default_kelulusan2': applicant.kelulusan2,
                    'default_tglmasukunv2': applicant.tglmasukunv2,
                    'default_tgllulus2': applicant.tgllulus2,
                    'default_ipk2': applicant.ipk2,
                    #Informasi Pendidikan 3#
                    'default_jenjang3' : applicant.jenjang3,
                    'default_namasekolah3': applicant.namasekolah3,
                    'default_jurusan3': applicant.jurusan3,
                    'default_kelulusan3': applicant.kelulusan3,
                    'default_tglmasukunv3': applicant.tglmasukunv3,
                    'default_tgllulus3': applicant.tgllulus3,
                    'default_ipk3': applicant.ipk3,
                    #Company History#
                    'default_namaperusahaan1' : applicant.namaperusahaan1,
                    'default_industri1' : applicant.industri1,
                    'default_jabatan1' : applicant.jabatan1,
                    'default_status1' : applicant.status1,
                    'default_jobdesc1' : applicant.jobdesc1,
                    'default_tglmasukperusahaan1' : applicant.tglmasukperusahaan1,
                    'default_tglresign1' : applicant.tglresign1,
                    'default_reason1' : applicant.reason1,
                    'default_salary1' : applicant.salary1,
                    #Company History#
                    'default_namaperusahaan2' : applicant.namaperusahaan2,
                    'default_industri2' : applicant.industri2,
                    'default_jabatan2' : applicant.jabatan2,
                    'default_status2' : applicant.status2,
                    'default_jobdesc2' : applicant.jobdesc2,
                    'default_tglmasukperusahaan2' : applicant.tglmasukperusahaan2,
                    'default_tglresign2' : applicant.tglresign2,
                    'default_reason2' : applicant.reason2,
                    'default_salary2' : applicant.salary2,
                    #Company History#
                    'default_namaperusahaan3' : applicant.namaperusahaan3,
                    'default_industri3' : applicant.industri3,
                    'default_jabatan3' : applicant.jabatan3,
                    'default_status3' : applicant.status3,
                    'default_jobdesc3' : applicant.jobdesc3,
                    'default_tglmasukperusahaan3' : applicant.tglmasukperusahaan3,
                    'default_tglresign3' : applicant.tglresign3,
                    'default_reason3' : applicant.reason3,
                    'default_salary3' : applicant.salary3,
                    #Skill
                    'default_bhsindtulis' : applicant.bhsindtulis,
                    'default_bhsindlisan' : applicant.bhsindlisan,
                    'default_bhsingtulis' : applicant.bhsingtulis,
                    'default_bhsinglisan' : applicant.bhsinglisan,
                    'default_word' : applicant.word,
                    'default_excel' : applicant.excel,
                    'default_powerpoint' : applicant.powerpoint,
                    'default_outlook' : applicant.outlook,
                    'default_csharp' : applicant.csharp,
                    'default_asp' : applicant.asp,
                    'default_vb' : applicant.vb,
                    'default_java' : applicant.java,
                    'default_objc' : applicant.objc,
                    'default_python' : applicant.python,
                    'default_php' : applicant.php,
                    'default_ruby' : applicant.ruby,
                    'default_sharepoint' : applicant.sharepoint,
                    'default_websphere' : applicant.websphere,
                    'default_tomcat' : applicant.tomcat,
                    'default_glassfish' : applicant.glassfish,
                    'default_android' : applicant.android,
                    'default_ios' : applicant.ios,
                    #REFRENSI KERJA
                    'default_namarefrensi1' : applicant.namarefrensi1,
                    'default_notelprefrensi1' : applicant.notelprefrensi1,
                    'default_hubunganref1' : applicant.hubunganref1,
                    'default_namarefrensi2' : applicant.namarefrensi2,
                    'default_notelprefrensi2' : applicant.notelprefrensi2,
                    'default_hubunganref2' : applicant.hubunganref2,
                    'default_psikotestconfirm' : applicant.psikotestconfirm,
                    'default_kontrakkerjaterakhir' : applicant.kontrakkerjaterakhir,
                    'default_hubrekankerjaterakhir' : applicant.hubrekankerjaterakhir,
                    'default_penghasilanlain' : applicant.penghasilanlain,
                    'default_department_id': applicant.department_id.id or False,
                    'default_address_id': applicant.company_id and applicant.company_id.partner_id
                            and applicant.company_id.partner_id.id or False,
                    'default_work_email': applicant.department_id and applicant.department_id.company_id
                            and applicant.department_id.company_id.email or False,
                    'default_work_phone': applicant.department_id.company_id.phone,
                    'form_view_initial_mode': 'edit',
                    'default_applicant_id': applicant.ids,
                    }
                    
        dict_act_window = self.env['ir.actions.act_window']._for_xml_id('hr.open_view_employee_list')
        dict_act_window['context'] = employee_data
        return dict_act_window
    
    #Private Information
    pasfoto = fields.Binary('Pas Foto',attachment=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    tempatlahir = fields.Char("Tempat Lahir")
    tanggallahir = fields.Date("Tanggal Lahir")
    agama = fields.Selection([('islam', 'Islam'), ('kristen protestan', 'Kristen Protestan'), 
    ('katolik', 'Kristen Katolik'),
    ('hindu', 'Hindu'),
    ('buddha', 'Buddha')],string='Agama', groups="hr.group_hr_user")
    nomorktp = fields.Char('Nomor KTP',website_form_blacklisted=False)
    alamatktp = fields.Char('Alamat Sesuai KTP')
    alamatsaatini = fields.Char('Alamat Saat ini (Jika Berbeda Dengan KTP)')
    emergencycontact = fields.Char('Emergency Contact')
    emergencyphone = fields.Char('Emergency Phone')
    sumber = fields.Char('Source')

    #Family Information - Ayah
    namaayah = fields.Char('Nama Ayah')
    tgllahirayah = fields.Date('Tanggal Lahir Ayah')
    pekerjaanayah = fields.Char('Pekerjaan Ayah')
    pendidikanayah = fields.Selection([('doktor', 'Doktor'), ('master', 'Master'), 
    ('sarjana', 'Sarjana'),
    ('diploma', 'Diploma'),
    ('sma', 'SMA'),('smp', 'SMP'),('sd', 'SD')],string='Pendidikan Ayah', groups="hr.group_hr_user")

    #Family Information - Ibu
    namaibu = fields.Char('Nama Ibu')
    tgllahiribu = fields.Date('Tanggal Lahir Ibu')
    pekerjaanibu = fields.Char('Pekerjaan Ibu')
    pendidikanibu = fields.Selection([('doktor', 'Doktor'), ('master', 'Master'), 
    ('sarjana', 'Sarjana'),
    ('diploma', 'Diploma'),
    ('sma', 'SMA'),('smp', 'SMP'),('sd', 'SD')],string='Pendidikan Ibu', groups="hr.group_hr_user")

    #Family Information - Saudara Kandung
    anakke = fields.Integer('Anak Ke ...')
    daribsdr = fields.Integer('Dari ... Bersaudara')

    #Family Information - Keluarga Inti
    marital = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced')
    ], string='Marital Status', groups="hr.group_hr_user", tracking=True)
    namapasangan = fields.Char('Nama Suami/Istri')
    tgllahirpasangan = fields.Date('Tanggal Lahir Sumi/Istri')
    pendpasangan = fields.Selection([('doktor', 'Doktor'), ('master', 'Master'), 
    ('sarjana', 'Sarjana'),
    ('diploma', 'Diploma'),
    ('sma', 'SMA'),('smp', 'SMP'),('sd', 'SD')],string='Jenis Kelamin', groups="hr.group_hr_user")
    pekpasangan = fields.Char('Pekerjaan Suami/Istri')
    jumlahanak = fields.Integer('Jumlah Anak')

    #Education Information
    jenjang1 = fields.Char('Jenjang Pendidikan')
    namasekolah1 = fields.Char('Nama Institusi')
    jurusan = fields.Char('Jurusan')
    kelulusan = fields.Selection([('none', 'None'), ('lulus', 'Lulus'), ('belum lulus', 'Belum Lulus'), 
    ('tidak dilanjutkan', 'Tidak Dilanjutkan'),
    ('drop out', 'Drop Out')],string='Status Kelulusan', groups="hr.group_hr_user")
    tglmasukunv = fields.Date('Tanggal Masuk')
    tgllulus = fields.Date('Tanggal Lulus')
    ipk = fields.Char('IPK / NEM')

    #Education Information
    jenjang2 = fields.Char('Jenjang Pendidikan2')
    namasekolah2 = fields.Char('Nama Institusi2')
    jurusan2 = fields.Char('Jurusan2')
    kelulusan2 = fields.Selection([('none', 'None'), ('lulus', 'Lulus'), ('belum lulus', 'Belum Lulus'), 
    ('tidak dilanjutkan', 'Tidak Dilanjutkan'),
    ('drop out', 'Drop Out')],string='Status Kelulusan2', groups="hr.group_hr_user")
    tglmasukunv2 = fields.Date('Tanggal Masuk')
    tgllulus2 = fields.Date('Tanggal Lulus2')
    ipk2 = fields.Char('IPK / NEM2')

    #Education Information
    jenjang3 = fields.Char('Jenjang Pendidikan3')
    namasekolah3 = fields.Char('Nama Institusi3')
    jurusan3 = fields.Char('Jurusan3')
    kelulusan3 = fields.Selection([('none', 'None'), ('lulus', 'Lulus'), ('belum lulus', 'Belum Lulus'), 
    ('tidak dilanjutkan', 'Tidak Dilanjutkan'),
    ('drop out', 'Drop Out')],string='Status Kelulusan3', groups="hr.group_hr_user")
    tglmasukunv3 = fields.Date('Tanggal Masuk3')
    tgllulus3 = fields.Date('Tanggal Lulus3')
    ipk3 = fields.Char('IPK / NEM3')

    #RIWAYAT PEKERJAAN 1
    namaperusahaan1 = fields.Char('Nama Perusahaan')
    industri1 = fields.Char('Industri')
    jabatan1 = fields.Char('Jabatan')
    status1 = fields.Selection([('none', 'None'), ('aktif', 'Aktif'),('resign', 'Resign')],string='Status Bekerja')
    jobdesc1 = fields.Char('Job Desc')
    tglmasukperusahaan1 = fields.Date('Tanggal Masuk')
    tglresign1 = fields.Date('Tanggal Resign')
    reason1 = fields.Char('Alasan pengunduran diri')
    salary1 = fields.Char('Gaji')

    #RIWAYAT PEKERJAAN 2
    namaperusahaan2 = fields.Char('Nama Perusahaan')
    industri2 = fields.Char('Industri')
    jabatan2 = fields.Char('Jabatan')
    status2 = fields.Selection([('none', 'None'), ('aktif', 'Aktif'),('resign', 'Resign')],string='Status Bekerja')
    jobdesc2 = fields.Char('Job Desc')
    tglmasukperusahaan2 = fields.Date('Tanggal Masuk')
    tglresign2 = fields.Date('Tanggal Resign')
    reason2 = fields.Char('Alasan pengunduran diri')
    salary2 = fields.Char('Gaji')
    
    #RIWAYAT PEKERJAAN 3
    namaperusahaan3 = fields.Char('Nama Perusahaan')
    industri3 = fields.Char('Industri')
    jabatan3 = fields.Char('Jabatan')
    status3 = fields.Selection([('none', 'None'), ('aktif', 'Aktif'),('resign', 'Resign')],string='Status Bekerja')
    jobdesc3 = fields.Char('Job Desc')
    tglmasukperusahaan3 = fields.Date('Tanggal Masuk')
    tglresign3 = fields.Date('Tanggal Resign')
    reason3 = fields.Char('Alasan pengunduran diri')
    salary3 = fields.Char('Gaji')

    #SKILL BAHASA
    bhsindtulis = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Bahasa Indonesia (Tulis)', groups="hr.group_hr_user", tracking=True)
    bhsindlisan = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Bahasa Indonesia (Lisan)', groups="hr.group_hr_user", tracking=True)
    bhsingtulis = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Bahasa Inggris (Tulis)', groups="hr.group_hr_user", tracking=True)
    bhsinglisan = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Bahasa Inggris (Lisan)', groups="hr.group_hr_user", tracking=True)
    
    #SKILL SOFTWARE
    word = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Microsoft Word', groups="hr.group_hr_user", tracking=True)
    excel = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Microsoft Excel', groups="hr.group_hr_user", tracking=True)
    powerpoint = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Microsoft Powerpoint', groups="hr.group_hr_user", tracking=True)
    outlook = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Microsoft Outlook', groups="hr.group_hr_user", tracking=True)
    
    #SKILL PROGRAMMING
    csharp = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='C#', groups="hr.group_hr_user", tracking=True)
    asp = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='ASP/ASP.NET', groups="hr.group_hr_user", tracking=True)
    vb = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='VB/VB.NET', groups="hr.group_hr_user", tracking=True)
    java = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='JAVA', groups="hr.group_hr_user", tracking=True)
    objc = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Objective C', groups="hr.group_hr_user", tracking=True)
    python = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Python', groups="hr.group_hr_user", tracking=True)
    php = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='PHP', groups="hr.group_hr_user", tracking=True)
    ruby = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Ruby', groups="hr.group_hr_user", tracking=True)

    #SKILL WEBSERVICE
    sharepoint = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Microsoft Sharepoint', groups="hr.group_hr_user", tracking=True)
    websphere = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='IBM Websphere', groups="hr.group_hr_user", tracking=True)
    tomcat = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Apache Tomcat', groups="hr.group_hr_user", tracking=True)
    glassfish = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Oracle Glassfish', groups="hr.group_hr_user", tracking=True)

    #MOBILE PROGRAMMING
    android = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Android', groups="hr.group_hr_user", tracking=True)
    ios = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='iOS', groups="hr.group_hr_user", tracking=True)

    #REFRENSI KERJA
    namarefrensi1 = fields.Char('Nama Refrensi 1')
    notelprefrensi1 = fields.Char('No Telp Refrensi 1')
    hubunganref1 = fields.Char('Hubungan Refrensi 1')
    namarefrensi2 = fields.Char('Nama Refrensi 2')
    notelprefrensi2 = fields.Char('No Telp Refrensi 2')
    hubunganref2 = fields.Char('Hubungan Refrensi 2')

    #INFORMASI TAMBAHAN
    psikotestconfirm = fields.Char('Keterangan Psikotest')
    kontrakkerjaterakhir = fields.Selection([('ya', 'Ya'), ('tidak', 'Tidak')], string='Terikat kontrak dengan tempat kerja terakhir?')
    hubrekankerjaterakhir = fields.Selection([('ya', 'Ya, saya keberatan'), 
    ('tidak', 'Tidak, saya tidak keberatan')], string='Keberatan menghubungi rekan kerja')
    penghasilanlain = fields.Char('Pekerjaan sampingan')
    penyakitkronis = fields.Char('Mengalami sakit kronis/operasi besar')
    perdin = fields.Selection([('ya', 'Ya'), ('tidak', 'Tidak')], string='Bersedia melakukan perjalanan dinas')
    penempatanluarkota = fields.Selection([('ya', 'Ya'), ('tidak', 'Tidak')], string='Bersedia ditempatkan diluar kota')
    salary_expected = fields.Char('Expected Salary')
    availability = fields.Selection([('secepatnya', 'Secepatnya'), ('1minggu', '1 Minggu'), 
    ('2/3minggu', '2/3 Minggu'), ('1bulan', '1 Bulan'), ('>1bulan', '>1 Bulan')], string='Expected Join Date')

class employeeData(models.Model):
    _inherit = 'hr.employee'

    #Private Information
    jenisklmn = fields.Selection([('male', 'Male'), ('female', 'Female')],string='Jenis Kelamin', groups="hr.group_hr_user")
    tempatlahir = fields.Char("Tempat Lahir")
    tanggallahir = fields.Date("Tanggal Lahir")
    agama = fields.Selection([('islam', 'Islam'), ('kristen protestan', 'Kristen Protestan'), 
    ('katolik', 'Kristen Katolik'),
    ('hindu', 'Hindu'),
    ('buddha', 'Buddha')],string='Agama', groups="hr.group_hr_user")
    nomorktp = fields.Char('Nomor KTP')
    alamatktp = fields.Char('Alamat Sesuai KTP')
    alamatsaatini = fields.Char('Alamat Saat ini (Jika Berbeda Dengan KTP)')
    emergencycontact = fields.Char('Emergency Contact')
    emergencyphone = fields.Char('Emergency Phone')
    sumber = fields.Char('Job Refrence')

    #Family Information - Ayah
    namaayah = fields.Char('Nama Ayah')
    tgllahirayah = fields.Date('Tanggal Lahir Ayah')
    pekerjaanayah = fields.Char('Pekerjaan Ayah')
    pendidikanayah = fields.Selection([('doktor', 'Doktor'), ('master', 'Master'), 
    ('sarjana', 'Sarjana'),
    ('diploma', 'Diploma'),
    ('sma', 'SMA'),('smp', 'SMP'),('sd', 'SD')],string='Jenis Kelamin', groups="hr.group_hr_user")

    #Family Information - Ibu
    namaibu = fields.Char('Nama Ibu')
    tgllahiribu = fields.Date('Tanggal Lahir Ibu')
    pekerjaanibu = fields.Char('Pekerjaan Ibu')
    pendidikanibu = fields.Selection([('doktor', 'Doktor'), ('master', 'Master'), 
    ('sarjana', 'Sarjana'),
    ('diploma', 'Diploma'),
    ('sma', 'SMA'),('smp', 'SMP'),('sd', 'SD')],string='Jenis Kelamin', groups="hr.group_hr_user")

    #Family Information - Saudara Kandung
    anakke = fields.Integer('Anak Ke ...')
    daribsdr = fields.Integer('Dari ... Bersaudara')

    #Family Information - Keluarga Inti
    namapasangan = fields.Char('Nama Suami/Istri')
    tgllahirpasangan = fields.Date('Tanggal Lahir Sumi/Istri')
    pendpasangan = fields.Selection([('doktor', 'Doktor'), ('master', 'Master'), 
    ('sarjana', 'Sarjana'),
    ('diploma', 'Diploma'),
    ('sma', 'SMA'),('smp', 'SMP'),('sd', 'SD')],string='Jenis Kelamin', groups="hr.group_hr_user")
    pekpasangan = fields.Char('Pekerjaan Suami/Istri')
    jumlahanak = fields.Integer('Jumlah Anak')

    #Education Information
    jenjang1 = fields.Char('Jenjang Pendidikan')
    namasekolah1 = fields.Char('Nama Institusi')
    jurusan = fields.Char('Jurusan')
    kelulusan = fields.Selection([('lulus', 'Lulus'), ('belum lulus', 'Belum Lulus'), 
    ('tidak dilanjutkan', 'Tidak Dilanjutkan'),
    ('drop out', 'Drop Out')],string='Status Kelulusan', groups="hr.group_hr_user")
    tglmasukunv = fields.Date('Tanggal Masuk')
    tgllulus = fields.Date('Tanggal Lulus')
    ipk = fields.Char('IPK / NEM')

    #Education Information
    jenjang2 = fields.Char('Jenjang Pendidikan2')
    namasekolah2 = fields.Char('Nama Institusi2')
    jurusan2 = fields.Char('Jurusan2')
    kelulusan2 = fields.Selection([('lulus', 'Lulus'), ('belum lulus', 'Belum Lulus'), 
    ('tidak dilanjutkan', 'Tidak Dilanjutkan'),
    ('drop out', 'Drop Out')],string='Status Kelulusan2', groups="hr.group_hr_user")
    tglmasukunv2 = fields.Date('Tanggal Masuk')
    tgllulus2 = fields.Date('Tanggal Lulus2')
    ipk2 = fields.Char('IPK / NEM2')

    #Education Information
    jenjang3 = fields.Char('Jenjang Pendidikan3')
    namasekolah3 = fields.Char('Nama Institusi3')
    jurusan3 = fields.Char('Jurusan3')
    kelulusan3 = fields.Selection([('none', 'None'), ('lulus', 'Lulus'), ('belum lulus', 'Belum Lulus'), 
    ('tidak dilanjutkan', 'Tidak Dilanjutkan'),
    ('drop out', 'Drop Out')],string='Status Kelulusan3', groups="hr.group_hr_user")
    tglmasukunv3 = fields.Date('Tanggal Masuk3')
    tgllulus3 = fields.Date('Tanggal Lulus3')
    ipk3 = fields.Char('IPK / NEM3')

    #RIWAYAT PEKERJAAN 1
    namaperusahaan1 = fields.Char('Nama Perusahaan')
    industri1 = fields.Char('Industri')
    jabatan1 = fields.Char('Jabatan')
    status1 = fields.Selection([ ('aktif', 'Aktif'),('resign', 'Resign')],string='Status Bekerja')
    jobdesc1 = fields.Char('Job Desc')
    tglmasukperusahaan1 = fields.Date('Tanggal Masuk')
    tglresign1 = fields.Date('Tanggal Resign')
    reason1 = fields.Char('Alasan pengunduran diri')
    salary1 = fields.Char('Gaji')

    #RIWAYAT PEKERJAAN 2
    namaperusahaan2 = fields.Char('Nama Perusahaan')
    industri2 = fields.Char('Industri')
    jabatan2 = fields.Char('Jabatan')
    status2 = fields.Selection([ ('aktif', 'Aktif'),('resign', 'Resign')],string='Status Bekerja')
    jobdesc2 = fields.Char('Job Desc')
    tglmasukperusahaan2 = fields.Date('Tanggal Masuk')
    tglresign2 = fields.Date('Tanggal Resign')
    reason2 = fields.Char('Alasan pengunduran diri')
    salary2 = fields.Char('Gaji')
    
    #RIWAYAT PEKERJAAN 3
    namaperusahaan3 = fields.Char('Nama Perusahaan')
    industri3 = fields.Char('Industri')
    jabatan3 = fields.Char('Jabatan')
    status3 = fields.Selection([ ('aktif', 'Aktif'),('resign', 'Resign')],string='Status Bekerja')
    jobdesc3 = fields.Char('Job Desc')
    tglmasukperusahaan3 = fields.Date('Tanggal Masuk')
    tglresign3 = fields.Date('Tanggal Resign')
    reason3 = fields.Char('Alasan pengunduran diri')
    salary3 = fields.Char('Gaji')

    #SKILL BAHASA
    bhsindtulis = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Bahasa Indonesia (Tulis)', groups="hr.group_hr_user", tracking=True)
    bhsindlisan = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Bahasa Indonesia (Lisan)', groups="hr.group_hr_user", tracking=True)
    bhsingtulis = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Bahasa Inggris (Tulis)', groups="hr.group_hr_user", tracking=True)
    bhsinglisan = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Bahasa Inggris (Lisan)', groups="hr.group_hr_user", tracking=True)
    
    #SKILL SOFTWARE
    word = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Microsoft Word', groups="hr.group_hr_user", tracking=True)
    excel = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Microsoft Excel', groups="hr.group_hr_user", tracking=True)
    powerpoint = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Microsoft Powerpoint', groups="hr.group_hr_user", tracking=True)
    outlook = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Microsoft Outlook', groups="hr.group_hr_user", tracking=True)
    
    #SKILL PROGRAMMING
    csharp = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='C#', groups="hr.group_hr_user", tracking=True)
    asp = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='ASP/ASP.NET', groups="hr.group_hr_user", tracking=True)
    vb = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='VB/VB.NET', groups="hr.group_hr_user", tracking=True)
    java = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='JAVA', groups="hr.group_hr_user", tracking=True)
    objc = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Objective C', groups="hr.group_hr_user", tracking=True)
    python = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Python', groups="hr.group_hr_user", tracking=True)
    php = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='PHP', groups="hr.group_hr_user", tracking=True)
    ruby = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Ruby', groups="hr.group_hr_user", tracking=True)

    #SKILL WEBSERVICE
    sharepoint = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Microsoft Sharepoint', groups="hr.group_hr_user", tracking=True)
    websphere = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='IBM Websphere', groups="hr.group_hr_user", tracking=True)
    tomcat = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Apache Tomcat', groups="hr.group_hr_user", tracking=True)
    glassfish = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Oracle Glassfish', groups="hr.group_hr_user", tracking=True)

    #MOBILE PROGRAMMING
    android = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='Android', groups="hr.group_hr_user", tracking=True)
    ios = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], string='iOS', groups="hr.group_hr_user", tracking=True)

    #REFRENSI KERJA
    namarefrensi1 = fields.Char('Nama Refrensi 1')
    notelprefrensi1 = fields.Char('No Telp Refrensi 1')
    hubunganref1 = fields.Char('Hubungan Refrensi 1')
    namarefrensi2 = fields.Char('Nama Refrensi 2')
    notelprefrensi2 = fields.Char('No Telp Refrensi 2')
    hubunganref2 = fields.Char('Hubungan Refrensi 2')

    #INFORMASI TAMBAHAN
    psikotestconfirm = fields.Char('Keterangan Psikotest')
    kontrakkerjaterakhir = fields.Selection([('ya', 'Ya'), ('tidak', 'Tidak')], string='Terikat kontrak dengan tempat kerja terakhir?')
    hubrekankerjaterakhir = fields.Selection([('ya', 'Ya, saya keberatan'), 
    ('tidak', 'Tidak, saya tidak keberatan')], string='Keberatan menghubungi rekan kerja')
    penghasilanlain = fields.Char('Pekerjaan sampingan')
    penyakitkronis = fields.Char('Mengalami sakit kronis/operasi besar')
    perdin = fields.Selection([('ya', 'Ya'), ('tidak', 'Tidak')], string='Keberatan melakukan perjalanan dinas')
    penempatanluarkota = fields.Selection([('ya', 'Ya'), ('tidak', 'Tidak')], string='Keberatan ditempatkan diluar kota')
    salary_expected = fields.Char('Expected Salary')

    @api.model
    def cron_reminder_birthday(self):
        today = fields.Date.context_today(self)
        employees = self.env['hr.employee'].search([
            ('birthday', '!=', False), 
            ('work_email', '!=', False)
        ])
        mail_channel_partner_obj = self.env['mail.channel.partner']
        odoobot = self.env.ref('base.partner_root')
        for employee in employees:
            if employee.user_id:
                users = self.env['res.users'].search([
                    ('id', '!=', False), 
                ])
            else:
                users = self.env['res.users'].search([])
            if employee.company_id.send_employee_reminder_birthday and employee.birthday.day == today.day and employee.birthday.month == today.month:
                template_id = self.env.ref('reminder_birthday.employee_reminder_birthday_template')
                if template_id:
                    template_id.send_mail(employee.id, force_send=True)

                message = _("Today is %s's birthday, congratulations!") % employee.name
                if users:
                    for user in users:
                        if employee.user_id and employee.user_id.id == user.id:
                            continue
                        if employee.company_id.id not in user.company_ids.ids:
                            continue
                        channel = mail_channel_partner_obj.sudo().search([
                            ('partner_id','=',user.partner_id.id),
                            ('channel_id.channel_type','=','chat'),
                            ('channel_id.channel_partner_ids.id','=',user.partner_id.id),
                            ('channel_id.public','=','private')
                            
                        ])
                        channel = channel.filtered(lambda x: len(x.channel_id.channel_partner_ids) == 1 and x.channel_id.is_chat == True and x.channel_id.member_count == 2)
                        if channel:
                            channel_send = channel.channel_id
                            if channel_send:
                                notification_ids = [(0, 0, {
                                    'res_partner_id': user.partner_id.id,
                                    'notification_type': 'inbox'
                                })]
                                channel_send.message_post(body=message, message_type="notification", subtype_xmlid="mail.mt_comment", 
                                    author_id=odoobot.id, 
                                    notification_ids=notification_ids)
                        else:
                            channel_send = self.env['mail.channel'].sudo().create({
                                'channel_partner_ids': [
                                    (4, user.partner_id.id),
                            
                                ],
                                'is_chat': True,
                                'public': 'private',
                                'channel_type': 'chat',
                                'name': odoobot.name + ', '+ user.partner_id.name,
                                
                                
                            })
                            if channel_send:
                                notification_ids = [(0, 0, {
                                    'res_partner_id': user.partner_id.id,
                                    'notification_type': 'inbox'
                                })]
                                channel_send.message_post(body=message, message_type="notification", subtype_xmlid="mail.mt_comment", 
                                    author_id=odoobot.id, 
                                    notification_ids=notification_ids)